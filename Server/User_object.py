import json


class User:
    """This is class of user"""

    def __init__(self, name="Ghost", password=""):
        self.rules = {"READ": False, "WRITE": False,
                      "CREATE": False, "ADMIN": False}
        self.password = password
        self.name = name
        self.database_users = "db_users.json"
        self.db = {f"name__{self.name}__": self.name,
                   f"password__{self.name}__": self.password, f"rules__{self.name}__": self.rules}

    def chek_usr(self):
        with open(self.database_users, "r", encoding="UTF-8") as f:
            user = json.load(f)
        if f"name__{self.name}__" not in user:
            return True
        else:
            return False

    def add_to_db(self):
        with open(self.database_users, "r", encoding="UTF-8") as f:
            usr = json.load(f)
        usr[f"name__{self.name}__"] = self.name
        usr[f"password__{self.name}__"] = self.password
        usr[f"rules__{self.name}__"] = self.rules
        with open(self.database_users, "w", encoding="UTF-8") as f:
            json.dump(usr, f)

    def rules_s(self):
        with open(self.database_users, "r", encoding="UTF-8") as f:
            usr = json.load(f)
            return usr[f"rules__{self.name}__"]

    def change_rules(self, role, znach=False):
        with open(self.database_users, "r", encoding="UTF-8") as f:
            usr = json.load(f)
        usr[f"rules__{self.name}__"][role] = znach
        with open(self.database_users, "w", encoding="UTF-8") as f:
            json.dump(usr, f)

    def del_user(self):
        with open(self.database_users, "r", encoding="UTF-8") as f:
            users = json.load(f)
        del users[f"name__{self.name}__"]
        del users[f"password__{self.name}__"]
        del users[f"rules__{self.name}__"]
        with open(self.database_users, "w", encoding="UTF-8") as f:
            json.dump(users, f)

    def chek_user(self):
        with open(self.database_users, "r", encoding="UTF-8") as f:
            usr = json.load(f)
        if self.name == usr[f"name__{self.name}__"] and self.password == usr[f"password__{self.name}__"]:
            return True
        else:
            return False

    def fc(self, dc):
        if dc == {}:
            return "no this function"
        else:
            if "name" in dc:
                name = dc["name"]
                with open(self.database_users, "r", encoding="UTF-8") as f:
                    usr = json.load(f)
                if f"name__{name}__" in usr:
                    return "Name using"
                else:    
                    usr[f"name__{name}__"], usr[f"password__{name}__"], usr[f"rules__{name}__"] = name, usr[
                        f"password__{self.name}__"], usr[f"rules__{self.name}__"]
                    del usr[f"name__{self.name}__"]
                    del usr[f"password__{self.name}__"]
                    del usr[f"rules__{self.name}__"]
                    with open(self.database_users, "w", encoding="UTF-8") as f:
                        usr = json.dump(usr, f)
                    return "Name change sucs"
            elif "password" in dc:
                password = dc["password"]
                with open(self.database_users, "r", encoding="UTF-8") as f:
                    usr = json.load(f)
                    usr[f"password__{self.name}__"] = password
                    with open(self.database_users, "w", encoding="UTF-8") as f:
                        usr = json.dump(usr, f)
                    return "Password changed sucs"
            elif "WRITE" in dc:
                with open("D:/ZAPROSI/zpr.txt", "a", encoding="UTF-8") as f:
                    f.write(f"#__{self.name}-WRITE___#")
                return "Wait, maybe i chage your rules"
            elif "READ" in dc:
                with open("D:/ZAPROSI/zpr.txt", "a", encoding="UTF-8") as f:
                    f.write(f"#__{self.name}-READ___#")
                return "Wait, maybe i chage your rules"
            elif "R_W" in dc:
                with open("D:/ZAPROSI/zpr.txt", "a", encoding="UTF-8") as f:
                    f.write(f"#__{self.name}-READ_AND_WRITE___#")
                return "Wait, maybe i chage your rules"
            
        