# Mock · AWS PaaS文档中心

# Mock

Mock测试就是在测试过程中，对于某些不容易构造或者不容易获取的对象，用一个虚拟的对象来创建以便测试的测试方法。 当Mock内容不为空时，在调用该DS模型时，不会向服务器端发送请求，将直接由Mock的值，进行数据清洗后返回。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/rds48.png)](<rds48.png>)

> Mock为了真实模拟DS调用，除了不向服务器端发送请求外，会执行默认值计算、数据清洗、脚本模式。