# skill-properties-demo

Demonstrates how defined properties can be utilized to change a skills behaviour using said properties.

## Properties definition

What (and how many) properties are defined is at the skill developers discretion. Properties are defined within the
`skill.yml definition`.

This demo can be configured using the `MANIPULATION_METHOD` property which is defined as following:
```
properties:
  - name: "MANIPULATION_METHOD"
    desc: "Configures how the skill manipulates requests"
    default: "UPPER"
    pattern: "(UPPER|LOWER|CAPITALIZE)"
```

If the property is omitted it will default to `UPPER` as defined. Using `pattern` allows the skill developer to
restrict the property values to the defined regex pattern. In this case the value can only be `UPPER`, `LOWER` or `CAPITALIZE`.

## Properties access

Properties can be accessed from the `context` in the defined handler module and function:
```
...
def evaluate(payload, context):
    manipulation_method = context.properties['MANIPULATION_METHOD']
...
```
or directly from the environment:
```
...
import os

def evaluate(payload, context):
    manipulation_method = os.environ.get('MANIPULATION_METHOD')
...
```

**NOTE:** Currently only the second method is supported
