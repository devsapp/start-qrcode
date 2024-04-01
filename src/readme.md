
> 注：当前项目为 Serverless Devs 应用，由于应用中会存在需要初始化才可运行的变量（例如应用部署地区、函数名等等），所以**不推荐**直接 Clone 本仓库到本地进行部署或直接复制 s.yaml 使用，**强烈推荐**通过 `s init ${模版名称}` 的方法或应用中心进行初始化，详情可参考[部署 & 体验](#部署--体验) 。

# start-qrcode-v3 帮助文档
<p align="center" class="flex justify-center">
    <a href="https://www.serverless-devs.com" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=start-qrcode-v3&type=packageType">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=start-qrcode-v3" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=start-qrcode-v3&type=packageVersion">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=start-qrcode-v3" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=start-qrcode-v3&type=packageDownload">
  </a>
</p>

<description>

本案例将qrcode，这一简单、方便的二维码生成器，快速创建并部署到阿里云函数计算 FC。

</description>

<codeUrl>

- [:smiley_cat: 代码](https://github.com/devsapp/start-qrcode/tree/V3/src)

</codeUrl>
<preview>



</preview>


## 前期准备

使用该项目，您需要有开通以下服务并拥有对应权限：

<service>



| 服务/业务 |  权限  | 相关文档 |
| --- |  --- | --- |
| 函数计算 |  AliyunFCFullAccess | [帮助文档](https://help.aliyun.com/product/2508973.html) [计费文档](https://help.aliyun.com/document_detail/2512928.html) |

</service>

<remark>



</remark>

<disclaimers>



</disclaimers>

## 部署 & 体验

<appcenter>
   
- :fire: 通过 [Serverless 应用中心](https://fcnext.console.aliyun.com/applications/create?template=start-qrcode-v3) ，
  [![Deploy with Severless Devs](https://img.alicdn.com/imgextra/i1/O1CN01w5RFbX1v45s8TIXPz_!!6000000006118-55-tps-95-28.svg)](https://fcnext.console.aliyun.com/applications/create?template=start-qrcode-v3) 该应用。
   
</appcenter>
<deploy>
    
- 通过 [Serverless Devs Cli](https://www.serverless-devs.com/serverless-devs/install) 进行部署：
  - [安装 Serverless Devs Cli 开发者工具](https://www.serverless-devs.com/serverless-devs/install) ，并进行[授权信息配置](https://docs.serverless-devs.com/fc/config) ；
  - 初始化项目：`s init start-qrcode-v3 -d start-qrcode-v3`
  - 进入项目，并进行项目部署：`cd start-qrcode-v3 && s deploy -y`
   
</deploy>

## 案例介绍

<appdetail id="flushContent">

本案例将qrcode，这一简单、方便的二维码生成器，快速创建并部署到阿里云函数计算 FC。

在Python中，有一个非常流行的库叫做 qrcode，它允许开发者在程序中生成二维码图像。本案例使用python将qrcode这个二维码生成库封装成函数，得到了一个弹性高可用的二维码服务。

通过 Serverless 开发平台，您只需要几步，就可以体验二维码生成器 ，并享受 Serverless 架构带来的降本提效的技术红利。

</appdetail>

## 使用流程

<usedetail id="flushContent">

### 查看部署的案例

项目部署完成，就得到了一个弹性高可用的二维码服务，直接使用生成的域名就可以得到期望的二维码， 比如获取 `AliyunFC` 的二维码, 直接在浏览器输入:

`http://qrcodefunc.qrcode.1431999136518149.cn-hangzhou.fc.devsapp.net/?data=AliyunFC`

![](https://img.alicdn.com/imgextra/i1/O1CN011z9tWP1s3gsAhX86V_!!6000000005711-0-tps-2536-1478.jpg)

**中文示例**

![](https://img.alicdn.com/imgextra/i4/O1CN013j2FT51we6pTSIlnF_!!6000000006332-0-tps-2492-1448.jpg)

**网址示例**

![](https://img.alicdn.com/imgextra/i1/O1CN01lfD9tI1hepDEzAw1I_!!6000000004303-0-tps-2452-1522.jpg)

### 二次开发

您可以通过云端控制台的开发功能进行二次开发。如果您之前是在本地创建的项目案例，也可以在本地项目目录`start-qrcode-v3`文件夹下，对项目进行二次开发。开发完成后，可以通过`s deploy`进行快速部署。

</usedetail>

## 注意事项

<matters id="flushContent">
</matters>


<devgroup>


## 开发者社区

您如果有关于错误的反馈或者未来的期待，您可以在 [Serverless Devs repo Issues](https://github.com/serverless-devs/serverless-devs/issues) 中进行反馈和交流。如果您想要加入我们的讨论组或者了解 FC 组件的最新动态，您可以通过以下渠道进行：

<p align="center">  

| <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407298906_20211028074819117230.png" width="130px" > | <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407044136_20211028074404326599.png" width="130px" > | <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407252200_20211028074732517533.png" width="130px" > |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| <center>微信公众号：`serverless`</center>                                                                                         | <center>微信小助手：`xiaojiangwh`</center>                                                                                        | <center>钉钉交流群：`33947367`</center>                                                                                           |
</p>
</devgroup>
