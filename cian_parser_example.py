import cianparser

print(cianparser.list_cities())

data = cianparser.parse(
    deal_type="sale",
    accommodation_type="flat",
    location="Екатеринбург",
    rooms=(1, 2, 3),
    start_page=1,
    end_page=2,
    is_saving_csv=True,
    is_latin=False,
    is_express_mode=False,
)

print(data[0])