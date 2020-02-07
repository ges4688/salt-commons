#!py

# The following statefile uses Python to set a grain ('sample-token') to
# a value pulled from a HTTP call. The call will not be repeated if the
# grain is already set.

from salt.utils.http import query
import json

def run():
  if __opts__['test']:
    return {
      'token': {
        'test.configurable_test_state': [
          {'name': 'sample-token'},
          {'result': True},
          {'changes': not grains.get('sample-token')}
        ]
      }
    }
  return {
   'token': {
     'grains.present': [
        {'name': 'sample-token'},
        {'value': grains.get('sample-token') or json.loads(
          query('http://jsonplaceholder.typicode.com/posts/1',
                decode_type=False)['body'])['id']}
      ]
    }
  }
