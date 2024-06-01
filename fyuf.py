  while(True):

        # js脚本
        random_id = [str(random.randint(0, 9)) for i in range(0,10)]
        random_id = "".join(random_id)
        random_id = 'id_input_target_url_' + random_id
        js = """
            // 弹出文本输入框，输入微信书的完整链接地址
            target_url = prompt("请输入微信书的完整链接地址","https://");
            
            // 动态创建一个input元素
            input_target_url = document.createElement("input");
            // 为其设置id，以便在程序中能够获取到它的值
            input_target_url.id = "id_input_target_url";
            
            // 插入到当前网页中
            document.getElementsByTagName("body")[0].appendChild(input_target_url);
            
            // 设置不可见
            document.getElementById("id_input_target_url").style.display = 'none';
            
            // 设置value为target_url的值
            document.getElementById("id_input_target_url").value = target_url
        """
        js = js.replace('id_input_target_url', random_id)


        # 执行以上js脚本
        driver.execute_script(js)

        # 判断弹出框是否存在
        while(True):
            try:
                # 检测是否存在弹出框
                alert = driver.switch_to.alert
                time.sleep(0.5)
            except:
                # 如果抛异常，说明当前页面不存在弹出框，即用户点击了取消或者确定
                break
