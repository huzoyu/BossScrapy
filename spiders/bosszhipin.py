# -*- coding: utf-8 -*-
import scrapy


class BosszhipinSpider(scrapy.Spider):
    name = 'bosszhipin'
    allowed_domains = ['www.zhipin.com']
    start_urls = [f'https://www.zhipin.com/c101270100-p100101/?page={i}&ka=page-{i}' for i in range(10)]

    def parse(self, response):
        # print(response.text)

        job_node_table = response.xpath("//*[@id=\"main\"]/div/div[2]/ul")
        job_node_list = job_node_table.xpath("./li")
        for job_node in job_node_list:
            enterprise_node = job_node.xpath("./div/div[2]/div/h3/a")
            salary_node = job_node.xpath("./div/div[1]/h3/a/span")
            requirement_node = job_node.xpath("./div/div[1]/p")
            time_node = job_node.xpath("./div/div[3]/p")

            enterprise = enterprise_node.xpath('string(.)')
            salary = salary_node.xpath('string(.)')
            requirement = requirement_node.xpath('string(.)')
            time = time_node.xpath('string(.)')


            print("企业", enterprise.extract_first().strip())
            print("薪资", salary.extract_first().strip())
            print("要求", requirement.extract_first().strip())
            print("更新", time.extract_first().strip())
            print()


        # meituan_node = response.xpath("//*[@id=\"main\"]/div/div[2]/ul/li[1]/div/div[2]/div/h3/a")  # 确定发布区的节点区域
        # meituan = meituan_node.xpath('string(.)')
        # print("企业", meituan.extract_first().strip())

        # content_left_node = response.xpath("//*[@id=\"main\"]/div/div[2]/ul")  # 确定发布区的节点区域


        # for div_node in div_node_list:
        #     enterprise_node = div_node.xpath("./li[1]/div/div[2]/div/h3/a")
        #     salary_node = div_node.xpath("./li[1]/div/div[1]/h3/a/span")
        #     requirement_node = div_node.xpath("./li[1]/div/div[1]/p")
        #
        #     # content = content_node.xpath('string(.)')
        #     print("企业", enterprise_node.extract_first().strip())
        #     print("薪资", salary_node.extract_first().strip())
        #     print("要求", requirement_node.extract_first().strip())

