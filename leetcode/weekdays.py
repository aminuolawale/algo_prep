class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        d = 31
        m = (8,)
        y = 2019
        w = "Saturday"
        ref = {"day": d, "month": m, "year": y, "weekday": "Saturday"}
        req = {"day": day, "month": month, "year": year, "weekday": None}
        weekdays = {
            "Sunday": 0,
            "Monday": 1,
            "Tuesday": 2,
            "Wednesday": 3,
            "Thursday": 4,
            "Friday": 5,
            "Saturday": 6,
        }
        months = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31,
        }
        ahead = False
        if self.gte(req, ref):
            ahead = True
            if ref["day"] == req["day"]:
                return ref["weekday"]
        else:
            diff = self.timed(req, ref)
        diff %= 7
        if ahead:
            k = weekdays.get("Saturday") + diff
        else:
            k = weekdays.get("Saturday") - diff
        k %= 7
        for w in weekdays:
            if weekdays[w] == k:
                return w

    def timed(a, b):
        result = 0
        g = None
        l = None
        if self.gte(a, b):
            g = a
            l = b
        else:
            g = b
            l = a
        while g != l:
            if g["month"] == l["month"] and g["year"] == l["year"]:
                result += months[l["month"]] - l["day"]
                break
            result += g["day"]
            g["month"] -= 1
            if g["month"] == 0:
                g["year"] -= 1
                g["month"] = 12
            g["day"] = months[g["month"]]
        result %= 7

        return result

    def gte(self, a, b):
        if a["year"] > b["year"]:
            return True
        elif a["year"] < b["year"]:
            return False
        else:
            if a["month"] > b["month"]:
                return True
            elif a["month"] < b["month"]:
                return False
            else:
                if a["day"] > b["day"]:
                    return True
                elif a["day"] < b["day"]:
                    return False
                return True


print(Solution().dayOfTheWeek(day=31, month=8, year=2019))
