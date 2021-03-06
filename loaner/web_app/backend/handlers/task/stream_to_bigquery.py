# Copyright 2018 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Streams an unstreamed BigQuery row to BigQuery."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import pickle
import webapp2

from loaner.web_app.backend.models import bigquery_row_model


class StreamToBigQueryHandler(webapp2.RequestHandler):
  """Handler for streaming a single queued row to BigQuery."""

  def post(self):
    payload = pickle.loads(self.request.body)
    row = bigquery_row_model.BigQueryRow.add(**payload)
    row.stream()
