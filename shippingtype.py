

class ShippingType:
    
    def paypalShippingTypes(self,shippingType):
        if shippingType == 1:
            return {
                'carrier': 'USPS', 
                'serviceType': 'PRIORITY_MAIL', 
                'packageType': 'PADDED_FLAT_RATE_ENVELOPE'
                }
        elif shippingType == 2:
            return {
                'carrier': 'USPS', 
                'serviceType': 'PRIORITY_MAIL', 
                'packageType': 'SMALL_FLAT_RATE_BOX'
                }
        elif shippingType == 3:
            return {
                'carrier': 'USPS', 
                'serviceType': 'PRIORITY_MAIL', 
                'packageType': 'FLAT_RATE_BOX'
                }
        elif shippingType == 4:
            return {
                'carrier': 'USPS', 
                'serviceType': 'PRIORITY_MAIL', 
                'packageType': 'LARGE_FLAT_RATE_BOX'
                }
        elif shippingType == 5:
            return {
                'carrier': 'USPS', 
                'serviceType': 'PRIORITY_MAIL', 
                'packageType': 'PACKAGE_OR_FLAT_ENVELOPE'
                }
        elif shippingType == 6:
            return {
                'carrier': 'USPS', 
                'serviceType': 'FIRST_CLASS_MAIL', 
                'packageType': 'PACKAGE_OR_FLAT_ENVELOPE'
                }