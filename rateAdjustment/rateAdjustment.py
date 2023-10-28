"""
Xét các biến sau để thực hiện thuật toán: 
- Thông tin của users
- Hũ Base ( Trong trường hợp demo mặc định là 50-30-20)
- Hũ Tháng trước : x-y-z (0.5, 0.3, 0.2)
- Thu nhập tháng trước: s
- Mức chi chi tiêu thực tế ở tháng trước (Tính theo tỉ lệ): real_x, real_y, real_z
- Thu nhập tháng này: new_s 
Đầu ra: Gợi ý tỷ lệ hũ mới cho tháng này: new_x, new_y, new_z
"""
import math


class rateAdjustment:
    def __init__(self, name, age):
        self.user = {"Name": f"{name}", "Age": age}
        self.base = "Normal"
        self.x = 0.5
        self.y = 0.3
        self.z = 0.2
        self.last_s = 1000000
        self.real_x = 0
        self.real_y = 0
        self.real_z = 0
        self.new_s = 0
        self.new_x = 0
        self.new_y = 0
        self.new_z = 0

    def getItem(self, real_x, real_y, real_z, new_s):
        self.real_x = real_x
        self.real_y = real_y
        self.real_z = real_z
        self.new_s = new_s

    def option(self):
        dif_s = self.new_s - self.last_s
        if dif_s == 0:
            Loss = (
                0.4 * (self.real_x - self.x)
                + 0.4 * (self.real_y - self.y)
                - 0.2 * (self.real_z - self.z)
            )
            # Update
            self.new_x = self.x - Loss * (
                (self.real_x - self.x) / abs(self.real_x - self.x)
            )
            self.new_y = self.y - Loss * (
                (self.real_y - self.y) / abs(self.real_y - self.y)
            )
            self.new_z = 1 - self.new_x - self.new_y

        elif dif_s > 0:
            Loss = (
                0.4 * (self.real_x - self.x)
                + 0.4 * (self.real_y - self.y)
                - 0.2 * (self.real_z - self.z)
            )
            # Update
            self.new_z = self.z + ((self.new_s / self.last_s) - 1) * 0.5
            self.new_x = (
                self.x + ((self.real_x - self.x) / abs(self.real_x - self.x)) * Loss
            )
            self.new_y = 1 - self.new_z - self.new_x

        else:
            Loss = (
                0.4 * (self.real_x - self.x)
                + 0.4 * (self.real_y - self.y)
                - 0.2 * (self.real_z - self.z)
            )
            # Update
            self.new_z = self.z - ((self.new_s / self.last_s) - 1) * 1.25
            self.new_x = (
                self.x + ((self.real_x - self.x) / abs(self.real_x - self.x)) * Loss
            )
            self.new_y = 1 - self.new_z - self.new_x

        print(dif_s)
        print(Loss)

    def update(self):
        self.x = self.new_x
        self.y = self.new_y
        self.z = self.new_z
        self.last_s = self.new_s


check = rateAdjustment("Bach", 19)
check.getItem(0.45, 0.35, 0.15, 1200000)
check.option()
print(check.new_x, check.new_y, check.new_z)
