import requests
keys = ["product_id","product_name","cat_id","autor","body","price","image","num_pages","ISBN"]

### API 1 ###

url = "http://gubitnik.com/api.php"

def test_length():
    response = requests.get("http://gubitnik.com/api.php").json()
    expected = 29
    assert expected == len(response)
    
test_length()


def test_all_keys():
    response_all = requests.get("http://gubitnik.com/api.php").json()
    keys = ["product_id","product_name","cat_id","autor","body","price","image","num_pages","ISBN"]
    for i in response_all:
        for key in keys:
            assert key in i
test_all_keys()

### API 2 ###

url = ("http://gubitnik.com/api.php?cat=2")

def test_lenght_specific_cat_id():
    response_specific_id = requests.get("http://gubitnik.com/api.php?cat=2").json()
    expected = 2
    assert expected == len(response_specific_id)
    
test_lenght_specific_cat_id()

def test_specific_category_id():
    response = requests.get("http://gubitnik.com/api.php").json()
    cat_id = set({})
    for cid in response:
        cat_id.add(cid["cat_id"])
    for cid in cat_id:
        response_cat = requests.get(f"http://gubitnik.com/api.php?cat={cid}").json()
        keys_all = {'product_id': '4', 'product_name': 'A.Makedonski', 'cat_id': '1', 'autor': 'Dzejn Bigam', 'body': '<p>Lorem ipsum dolor sit amet sed do eiusmod.Lorem ipsum dolor sit amet sed do eiusmod.Lorem ipsum dolor sit amet sed do eiusmod.Lorem ipsum dolor sit amet sed do eiusmod.Lorem ipsum dolor sit amet sed do eiusmod.Lorem ipsum dolor sit amet sed do eiusmod.Lorem ipsum dolor sit amet sed do eiusmod.Lorem ipsum dolor sit amet sed do eiusmod.Lorem ipsum dolor sit amet sed do eiusmod.Lorem ipsum dolor sit amet sed do eiusmod.</p>', 'price': '505.22', 'image': 'aleksandar-makedonski.jpg', 'num_pages': '372', 'ISBN': '978-86-521-2152-6'}
        keys_all = tuple(keys_all.keys())
        assert keys_all == ("product_id","product_name","cat_id","autor","body","price","image","num_pages","ISBN")
test_specific_category_id()



### API 3 ###

url = ("http://gubitnik.com/api.php?id=4")

def test_lenght_prod_id():
    response_prod_id = requests.get("http://gubitnik.com/api.php?id=4").json()
    expected = 9
    assert expected == len(response_prod_id)
test_lenght_prod_id()


def test_product_id():
    response_prod_id = [p["product_id"] for p in requests.get("http://gubitnik.com/api.php?").json()]
    for pid in response_prod_id:
        response = requests.get(f"http://gubitnik.com/api.php?id={pid}").json()
        keys_all = {'product_id': '4', 'product_name': 'A.Makedonski', 'cat_id': '1', 'autor': 'Dzejn Bigam', 'body': '<p>Lorem ipsum dolor sit amet sed do eiusmod.Lorem ipsum dolor sit amet sed do eiusmod.Lorem ipsum dolor sit amet sed do eiusmod.Lorem ipsum dolor sit amet sed do eiusmod.Lorem ipsum dolor sit amet sed do eiusmod.Lorem ipsum dolor sit amet sed do eiusmod.Lorem ipsum dolor sit amet sed do eiusmod.Lorem ipsum dolor sit amet sed do eiusmod.Lorem ipsum dolor sit amet sed do eiusmod.Lorem ipsum dolor sit amet sed do eiusmod.</p>', 'price': '505.22', 'image': 'aleksandar-makedonski.jpg', 'num_pages': '372', 'ISBN': '978-86-521-2152-6'}
        keys_all = tuple(keys_all.keys())
        assert keys_all == ("product_id","product_name","cat_id","autor","body","price","image","num_pages","ISBN")
test_product_id()


