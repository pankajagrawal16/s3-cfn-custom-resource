# s3-cfn-custom-resource
Playing with lambda based custom resources. It deploys lambda based custom resources via SAM.

# Test locally
You can customise and test your logic based on sample events template. Also note with Pycharm IDE you can now debug your lambda function step by step.
Checkout [blog](https://aws.amazon.com/blogs/aws/new-aws-toolkits-for-pycharm-intellij-preview-and-visual-studio-code-preview/).  Also in case of access issue refer blog [here](https://medium.com/@malzoek/debugging-lambdas-locally-with-pycharm-d64b5260c165)

```
    sam local invoke  --event events/event.json
```

#Steps to deploy

Build your sam resources:

```
    sam build -t custom-resources.cfn.yml --use-container 
```

Deploy your SAM resources:

```
    sam deploy --stack-name s3-custom-resources --region us-east-1 --s3-bucket sam-custom-lambda-base --capabilities CAPABILITY_IAM 
```

# Testing

There is a sample template on how this custom resource can be used in your cloud formation templates.

```
    aws cloudformation create-stack --stack-name example-s3-bucket --template-body file://example/template.yml --parameters ParameterKey=BucketName,ParameterValue=awsome-s3-bucket --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND CAPABILITY_IAM
```


