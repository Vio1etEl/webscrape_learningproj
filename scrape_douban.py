# Name: El
# Time: 2024/3/13 19:53
import requests
from bs4 import BeautifulSoup
for i in range(0,250,25):
    url = f'https://movie.douban.com/top250?start={i}'
    headers = {
        'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36'
    }
    response = requests.get(url,headers=headers)
    # print(response.status_code)  # 判断是否正常访问 200
    content = response.text
    soup = BeautifulSoup(content,'html.parser')
    all_title = soup.findAll('span',attrs={'class':'title'})  # 获取所有 'class'='title' 的span标签对象
    for title_name in all_title:
        if '/' not in title_name.string:
            print(title_name.string)
"""
HTML 常见标签
1. 标题标签 
<h1>这是一个一级标签</h1>
<h2>这是一个二级标签</h2>

2. 文本标签
<p>XXX</p>  # 自动换行
<p>XXX<br>XXX</p>  # <br> 换行标签，无闭合标签
    <b>XXX</b>  # 加粗
    <i>XXX</i>  # 斜体
    <u>XXX</u>  # 加下划线

3. 图片标签  # 无闭合标签
<img scr="XXX"  >  # scr = source 图片路径/链接

4. 链接标签
<a href="XXX(要跳转的URL链接)"target="_self">XXX(文字内容)</a>
    target="_self"  # 选填表示直接在当前窗口跳转链接
    target="_blank"  # 在新窗口跳转

5. 容器标签
5.1 
    <div>  # 块级元素,独占一块,一行最多放一个 <div> 元素
        XXX
    </div>

5.2  
    <span>  # 内联元素, 一行可以有多个
        XXX
    </span>

6. 列表元素
6.1 有序列表  # 列表内的元素要用 <li> 标签
    <ol>  # ordered list简写
        <li>XX</li>  # 1.XX
        <li>XX</li>  # 2.XX
    </ol>

6.2 无序列表
    <ul>  # 没有数字排序 用点或者小横杠
        <li>XX</li>  # ·XX
        <li>XX</li>  # ·XX
    </ul>
        
7. 表格标签
    <table>
        <thead>  # 表头, 表格第一行
            <tr>  # 表行 table row
                <td>XXX</td>  # table data
                <td>CCC</td>
            </tr>
        </thead>
        <tbody>  # 表格主体
            <tr>
                <td>111</td>
                <td>222</td>
            <tr>
        </tbody>
    </table>

8. class
    <p class="content">给岁月以文明</p>
    # class 可以在所有标签内运用 定义类帮助分组

"""