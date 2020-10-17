import decimal
import json

# This is a workaround for: http://bugs.python.org/issue16535
# Residual of bython bug, dont dear to remove
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return int(obj)
        return super(DecimalEncoder, self).default(obj)
