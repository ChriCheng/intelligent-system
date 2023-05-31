class ProductionRule:
    @staticmethod
    def store_rule(rule):
        # 将规则存储在文本文件中
        with open("rules.txt", "a") as file:
            file.write(rule + "\n")
        print("规则已存储")

    @staticmethod
    def delete_rule(rule):
        # 从文本文件中删除规则
        with open("rules.txt", "r") as file:
            lines = file.readlines()
        with open("rules.txt", "w") as file:
            for line in lines:
                if line.strip() != rule:
                    file.write(line)
        print("规则已删除")

    @staticmethod
    def check_rule(query):
        # 检查指定规则是否存在
        with open("rules.txt", "r") as file:
            rules = file.readlines()
        for rule in rules:
            if rule.strip() == query:
                print("规则存在")
                return True
        print("规则不存在")
        return False

    @staticmethod
    def show_rules():
        # 展示已有规则
        with open("rules.txt", "r") as file:
            rules = file.readlines()
        print("已有规则：")
        for rule in rules:
            print(rule.strip())
