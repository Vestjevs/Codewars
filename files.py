import os
import os.path
import shutil


class ExFiles:

    def method1(self, k):
        """
        Documentation for this method1


        uses range for multiple values between 0 - k
        """
        for i in range(k):
            j = i * i
            return j


print(ExFiles.method1.__doc__)
