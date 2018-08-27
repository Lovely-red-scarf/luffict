这是一个商城购物车功能
使用了 Django1.1+python3.5然后widows功能开发
数据库使用了最简单的sqllite  然后购物车信息使用的redis 数据库 内部使用的时候注意配置

后台admin功能登陆账户: root  密码：root1234

虽然只实现了一个购物车 支付和订单界面是基于购物车给做的

api这个app中放置的是主要的代码逻辑
app01主要是models数据库的生成  

api中的views中放置了 三个主要的流程登陆auth  然后shopping_car是购物车的流程  payment是支付（只写了一部分感觉都是重复逻辑）
api中的utils放置的是一些中间状态需要的逻辑 auth是登陆认证 response是对字典进行类的生成
