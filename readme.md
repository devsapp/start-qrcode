# start-qrcode 帮助文档

<p align="center" class="flex justify-center">
    <a href="https://www.serverless-devs.com" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=start-qrcode&type=packageType">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=start-qrcode" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=start-qrcode&type=packageVersion">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=start-qrcode" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=start-qrcode&type=packageDownload">
  </a>
</p>

<description>

>  ***快速部署一个生成二维码的应用到阿里云函数计算***

</description>

<table>
</table>

<codepre id="codepre">
</codepre>

<deploy>

## 部署 & 体验

<appcenter>

-  :fire:  通过 [Serverless 应用中心](https://fcnext.console.aliyun.com/applications/create?template=start-qrcode) ，
[![Deploy with Severless Devs](https://img.alicdn.com/imgextra/i1/O1CN01w5RFbX1v45s8TIXPz_!!6000000006118-55-tps-95-28.svg)](https://fcnext.console.aliyun.com/applications/create?template=start-qrcode)  该应用。 

</appcenter>

- 通过 [Serverless Devs Cli](https://www.serverless-devs.com/serverless-devs/install) 进行部署：
    - [安装 Serverless Devs Cli 开发者工具](https://www.serverless-devs.com/serverless-devs/install) ，并进行[授权信息配置](https://www.serverless-devs.com/fc/config) ；
    - 初始化项目：`s init start-qrcode -d start-qrcode`   
    - 进入项目，并进行项目部署：`cd start-qrcode && s deploy -y`

</deploy>

<appdetail id="flushContent">

# 应用详情

项目部署完成，就得到了一个弹性高可用的二维码服务，直接使用生成的域名就可以得到期望的二维码， 比如获取 `AliyunFC` 的二维码, 直接在浏览器输入:

`http://qrcodefunc.qrcode.1431999136518149.cn-hangzhou.fc.devsapp.net/?data=AliyunFC`

![](https://img.alicdn.com/imgextra/i4/O1CN018KjUON1pnztVvxBTq_!!6000000005406-2-tps-2576-1132.png)

**中文示例**

![](https://img.alicdn.com/imgextra/i4/O1CN01c2tKoT24cI0U2ivUc_!!6000000007411-2-tps-2596-1100.png)

**网址示例**

![](https://img.alicdn.com/imgextra/i1/O1CN01w6JHGc1mgikpsRckn_!!6000000004984-2-tps-2552-1168.png)

</appdetail>

<devgroup>

## 开发者社区

您如果有关于错误的反馈或者未来的期待，您可以在 [Serverless Devs repo Issues](https://github.com/serverless-devs/serverless-devs/issues) 中进行反馈和交流。如果您想要加入我们的讨论组或者了解 FC 组件的最新动态，您可以通过以下渠道进行：

<p align="center">

| <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407298906_20211028074819117230.png" width="130px" > | <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407044136_20211028074404326599.png" width="130px" > | <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407252200_20211028074732517533.png" width="130px" > |
|--- | --- | --- |
| <center>微信公众号：`serverless`</center> | <center>微信小助手：`xiaojiangwh`</center> | <center>钉钉交流群：`33947367`</center> | 

</p>

</devgroup>