#
#  Copyright 2019 The FATE Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

import argparse

import pandas as pd
import xgboost as xgb
from sklearn.metrics import roc_auc_score, precision_score, accuracy_score, recall_score

from pipeline.utils.tools import JobConfig


def main(param="./xgb_config_multi.yaml"):
    # obtain config
    if isinstance(param, str):
        param = JobConfig.load_from_file(param)
    data_guest = param["data_guest"]
    data_host = param["data_host"]

    idx = param["idx"]
    label_name = param["label_name"]

    # prepare data
    df_guest = pd.read_csv(data_guest, index_col=idx)
    df_host = pd.read_csv(data_host, index_col=idx)
    df = df_guest.join(df_host, rsuffix='host')
    y = df[label_name]
    X = df.drop(label_name, axis=1)

    train_data = xgb.DMatrix(data=X, label=y)
    xgb_param = {'max_depth': 3, "eta": 0.1, 'objective': 'multi:softmax', 'num_class': 4}
    eval_list = [(train_data, 'train')]
    boosting_round = 10

    xgb_model = xgb.train(xgb_param, train_data, num_boost_round=boosting_round, evals=eval_list)
    y_pred = xgb_model.predict(train_data)

    try:
        auc_score = roc_auc_score(y, y_pred)
    except:
        print(f"no auc score available")
        

    result = {}
    recall = recall_score(y, y_pred, average=None)
    pr = precision_score(y, y_pred, average=None)
    acc = accuracy_score(y, y_pred)
    result = {"recall": recall.sum()/len(recall), "precision": pr.sum()/len(pr), "accuracy": acc}
    print('multi result', result)
    return {}, result


if __name__ == "__main__":
    parser = argparse.ArgumentParser("BENCHMARK-QUALITY SKLEARN JOB")
    parser.add_argument("-param", type=str,
                        help="config file for params")
    args = parser.parse_args()
    if args.config is not None:
        main(args.param)
    main()
