# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from typing import List, Dict, Any

from hugegraph_llm.utils.log import log


class ContentValidator:
    def __init__(self):
        pass

    def validate_content_contains_keywords(self, content: str, context: Dict[str, Any]):
        keywords = context["keywords"] or []
        for keyword in keywords:
            if keyword not in content:
                log.debug(f"内容不包含关键词: {keyword}")
                return False
        return True

    def run(self, context: Dict[str, Any]) -> Dict[str, Any]:
        if context["graph_result_flag"] != 0:
            return context
        if self.validate_content_contains_keywords(content="\n".join(context["graph_result"]), context=context):
            context["graph_result_flag"] = 0
        else:
            context["graph_result_flag"] = -1
            context["graph_result"] = ""
        return context
