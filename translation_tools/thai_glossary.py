# Thai Glossary Terms
# Auto-generated from Translation Tools
# This file contains Thai translations for common business terms

thai_glossary = {
    # Category: Business
    'Account': 'บัญชี',
    # Context: ERPNext มีฟีเจอร์ Account Freezing สำหรับป้องกันไม่ให้มีการบันทึกหรือแก้ไขเอกสารบัญชีย้อนหลังหลังจากวันที่กำหนด | Category: Business
    'Account Freezing': 'การอายัดบัญชี / ระงับบัญชี',
    # Category: Business
    'Accounting': 'การบัญชี',
    # Category: Technical
    'All': 'ทั้งหมด',
    # Category: Business
    'Assets': 'สินทรัพย์',
    # Category: Technical
    'Business': 'ธุรกิจ',
    # Category: Business
    'Buying': 'การซื้อ',
    # Category: Status
    'Cancelled': 'ยกเลิก',
    # Category: Technical
    'Category': 'หมวดหมู่',
    # Category: Status
    'Completed': 'เสร็จสิ้น',
    # Category: Technical
    'Context': 'บริบท',
    # Category: Technical
    'CRM': 'การบริหารลูกค้าสัมพันธ์',
    # Category: Business
    'Customer': 'ลูกค้า',
    # Category: Date/Time
    'Date': 'วันที่',
    # Category: Date/Time
    'Date and Time': 'วันที่และเวลา',
    # Category: Date/Time
    'Date/Time': 'วัน/เวลา',
    # Category: Date/Time
    'Day': 'วัน',
    # Category: Business
    'Delivery Note': 'ใบส่งสินค้า',
    # Category: Business
    'Description': 'รายละเอียด',
    # Category: Status
    'Draft': 'ฉบับร่าง',
    # Category: Technical
    'ERPNext Module': 'โมดูล ERPNext',
    # Category: Business
    'Human Resources': 'ทรัพยากรบุคคล',
    # Category: Business
    'Inventory': 'คลังสินค้า',
    # Category: Business
    'Invoice': 'ใบแจ้งหนี้',
    # Category: Status
    'Is Approved': 'อนุมัติแล้ว',
    # Category: Status
    'Is Rejected': 'ปฏิเสธแล้ว',
    # Category: Business
    'Item': 'สินค้า',
    # Category: Business
    'Journal Entry': 'บันทึกทางบัญชี',
    # Category: UI
    'Loading translation dashboard...': 'กำลังโหลดกระดานข้อมูลแปลภาษา',
    # Category: Business
    'Manufacturing': 'การผลิต',
    # Category: Technical
    'Module': 'โมดูล',
    # Category: Technical
    'Module Name': 'ชื่อ โมดูล',
    # Category: Date/Time
    'Month': 'เดือน',
    # Category: Status
    'Paid': 'ชำระแล้ว',
    # Category: Business
    'Payment': 'การชำระเงิน',
    # Category: Status
    'Pending': 'รอดำเนินการ',
    # Category: UI
    'Print Message': 'พิมพ์ข้อความ',
    # Category: UI
    'Priority': 'ลำดับความสำคัญ',
    # Category: Business
    'Projects': 'โครงการ',
    # Category: Business
    'Purchase Invoice': 'ใบแจ้งหนี้ซื้อ',
    # Category: Business
    'Purchase Order': 'ใบสั่งซื้อ',
    # Category: Business
    'Purchases': 'ซื้อ',
    # Category: Business
    'Quantity': 'จำนวน',
    # Category: Business
    'Quotation': 'ใบเสนอราคา',
    # Category: Business
    'Receipt': 'ใบเสร็จรับเงิน',
    # Category: UI
    'Refresh': 'ดึงข้อมูลใหม่',
    # Category: Business
    'Sales': 'ขาย',
    # Category: Business
    'Sales Invoice': 'ใบแจ้งหนี้ขาย',
    # Category: Business
    'Sales Order': 'ใบสั่งขาย',
    # Category: Business
    'Selling': 'การขาย',
    # Category: UI
    'Source Term': 'แหล่งข้อมูล',
    # Category: Status
    'Status': 'สถานะ',
    # Category: Business
    'Stock': 'คลังสินค้า',
    # Category: Status
    'Submitted': 'ส่งแล้ว',
    # Category: Business
    'Supplier': 'ผู้จัดจำหน่าย',
    # Category: Business
    'Tax': 'ภาษี',
    # Category: Business
    'Tax Invoice': 'ใบกำกับภาษี',
    # Category: UI
    'Thai Translation': 'แปลเป็นไทย',
    # Category: Date/Time
    'Time': 'เวลา',
    # Category: UI
    'Translation Dashboard': 'กระดานข้อมูลแปลภาษา',
    # Category: Business
    'Unit Price': 'ราคาต่อหน่วย',
    # Category: Business
    'VAT': 'ภาษีมูลค่าเพิ่ม',
    # Category: Business
    'Withholding Tax': 'ภาษีหัก ณ ที่จ่าย',
    # Category: Date/Time
    'Year': 'ปี',

}

def get_thai_translation(english_term):
    """Get Thai translation for an English term"""
    return thai_glossary.get(english_term, english_term)

def get_all_terms():
    """Get all glossary terms"""
    return thai_glossary
