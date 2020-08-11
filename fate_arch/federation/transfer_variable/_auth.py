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

import itertools
import json
import typing
from pathlib import Path

import yaml

_transfer_auth: typing.Optional[typing.MutableMapping] = None

_TRANSFER_CONF_PATH = "../../../conf/transfer_conf.yaml"


def _get_transfer_conf():
    global _transfer_auth
    if _transfer_auth is not None:
        return _transfer_auth

    _transfer_auth = {}
    path = Path(__file__).parent.joinpath(_TRANSFER_CONF_PATH).resolve()
    if not path.is_file():
        raise NameError(f"transfer variable path conf: {path} not found")

    with open(path) as f:
        conf = yaml.load(f)

    transfer_conf_files = []
    for base_dir in conf.get('paths', []):
        full_path = path.parent.joinpath(base_dir)
        if full_path.is_file():
            if full_path.suffix == ".json":
                transfer_conf_files.append([full_path])
            else:
                raise NameError(f"{full_path} not supported")
        else:
            transfer_conf_files.append(full_path.glob("**/*.json"))

    for a_conf in itertools.chain(*transfer_conf_files):
        try:
            with a_conf.open() as f:
                _transfer_auth.update(json.load(f))
        except Exception as e:
            raise RuntimeError(f"parse {a_conf} fail: {e.args}")

    return _transfer_auth


def _check_variable_auth_conf(full_name):
    module_name, class_name, variable_name = full_name.split("$")
    variable_auth = _get_transfer_conf().get(f"{module_name}.{class_name}", {}).get(variable_name, None)
    if variable_auth is None:
        if f"{module_name}.{class_name}" not in _get_transfer_conf():
            raise NameError(f"{module_name}.{class_name} not found")
        else:
            raise NameError(f"{variable_name} not found in {module_name}.{class_name}")

    auth_src = variable_auth["src"]
    if not isinstance(auth_src, list):
        auth_src = [auth_src]
    auth_dst = variable_auth["dst"]
    if not isinstance(auth_dst, list):
        auth_dst = [auth_dst]

    return auth_src, auth_dst
