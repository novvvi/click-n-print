import os, sys, traceback
from paypal import Paypal
from shippingtype import ShippingType
from googlesheet import GSheet
from dotenv import load_dotenv
import time
load_dotenv()

class Main:

    def __init__(self):
        self.gs = GSheet()
        self.pp = Paypal(os.getenv("PAYPAL_USER"),os.getenv("PAYPAL_PASS"), ShippingType())
        self.listOfLabelInfo = self.gs.getAll()

    def run(self):
        self.pp.login()
        for info in self.listOfLabelInfo:
            while True:
                try:
                    self.pp.getLabel(info)
                    time.sleep(5)
                except Exception as e:
                    print(str(e))
                    traceback.print_exc() 
                    time.sleep(20)
                    continue
                break

    def printing(self):
        print(self.listOfLabelInfo)


if __name__ == "__main__":
    main = Main()
    main.run()