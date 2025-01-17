# 项目说明

安装依赖，运行程序web.py

```
pip install -r requirements.txt
python web.py 
```

启动后访问 http://127.0.0.1:5000/get_data?username=你的学号&password=你的密码  即会返回完整json信息

正常情况下获取到的json内容为：

```
{
"allinfo":详细的个人信息,
"notifications": 通知消息,
"current_time": 查询时间,
"integrated_info": 简略个人信息,
"integrated_grade_info": 成绩信息（处理后）,
"selected_courses_filtering": 未公布成绩的课程和异常的课程,
"run_log": 运行日志（暂未遇到非空情况）,
"error_content": 错误日志（暂未遇到非空情况）
}    
```

错误情况下获取到的json内容为：

```
{
"error": 错误原因（如：学号或密码错误）
}
```

## 许可证

`Copyright © 2024 NianBroken. All rights reserved.`

本项目采用 [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0 "Apache-2.0") 许可证。简而言之，你可以自由使用、修改和分享本项目的代码，但前提是在其衍生作品中必须保留原始许可证和版权信息，并且必须以相同的许可证发布所有修改过的代码。

## 特别感谢

[openschoolcn/zfn_api](https://github.com/openschoolcn/zfn_api "openschoolcn/zfn_api")

[https://github.com/NianBroken/ZFCheckScores/](https://github.com/NianBroken/ZFCheckScores/)
