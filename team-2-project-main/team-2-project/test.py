import pandas as pd
import pandas.testing as pd_testing
import numpy
import hashlib
import datetime
from unittest.mock import patch, Mock
from et_pipeline.extract import extract_file
from et_pipeline.transform_sensitive_data import remove_sensitive_data
from et_pipeline.transform_3NF_customer import customer_normalised
from et_pipeline.transform_3NF_payment_type import payment_type_normalised
from et_pipeline.transform_3NF_product_flavour import product_flavour_normalised
from et_pipeline.transform_3NF_product_size import product_size_normalised
from et_pipeline.transform_3NF_store import store_normalised
from et_pipeline.transform_3NF_orders import orders_normalised
from et_pipeline.transform_3NF_product import product_normalised
from et_pipeline.transform_3NF_order_item import order_item_normalized
# NEED TO UNIT TEST ET_LAMBDA_FUNCTION WITH MOTO
# NEED TO UNIT TEST EXTRACT_TRANSFORM_PIPELINE WITH MOTO
# NEED TO UNIT TEST DATABASE_MANAGER WITH MOTO
# NEED TO UNIT TEST LOAD_LAMBDA_FUNCTION WITH MOTO
# NEED TO UNIT TEST LOADING


@patch("et_pipeline.extract.pd.read_csv")
def test_1_opening_extract_file(mock_extract_file: Mock):
    # Assemble
    expected = 5
    mock_extract_file.return_value = 5
    
    # Act
    result = extract_file("test_data.csv")
    
    # Assert
    assert expected == result

def test_2_opening_extract_file():
    # Assemble
    data = {'timestamp': ['21/08/2021 00:00', '22/08/2021 00:00', '23/08/2021 00:00', '24/08/2021 00:00', '25/08/2021 00:00'],
            'store_name': ['Manchester','Manchester','Manchester','Manchester','Manchester'],
            'customer_name': ['Tony','Sol','Jose','Candy','Nelly'],
            'basket_items': ['Regular Flavoured iced latte - Hazelnut - 2.55','Large Flavoured mocha - Caramel - 2.55','Regular latte - 2.55','Large Flavoured latte - Vanilla - 2.55','Regular Flavoured latte - Coffee - 2.55,Regular Flavoured latte - Coffee - 2.55'],
            'total_price': [2.55, 2.55, 2.55, 2.55, 3.10],
            'payment_type_name': ['CARD', 'CARD', 'CASH', 'CARD', 'CASH'],
            'card_number': [numpy.NaN, numpy.NaN, numpy.NaN, numpy.NaN, numpy.NaN]}
    expected = pd.DataFrame(data=data)
    
    # Act
    result = extract_file("test_data.csv")
    
    # Assert
    pd_testing.assert_frame_equal(expected,result)

def test_1_remove_sentive_data():
    # Assemble
    data_1 = {'col1': [1, 2], 'col2': [3, 4]}
    data_2 = {'col1': [1, 2]}
    dataframe_1 = pd.DataFrame(data=data_1)
    dataframe_2 = pd.DataFrame(data=data_2)
    expected = dataframe_2
    
    # Act
    result = remove_sensitive_data(dataframe_1,['col2'])
    
    # Assert
    assert all(expected == result)


@patch("et_pipeline.transform_sensitive_data.pd.DataFrame.drop")
def test_2_remove_sentive_data(mock_remove_sensitive_data: Mock):
    # Assemble
    expected = 5
    mock_remove_sensitive_data.return_value = 5
    data_1 = {'col1': [1, 2], 'col2': [3, 4]}
    dataframe_1 = pd.DataFrame(data=data_1)
    
    # Act
    result = remove_sensitive_data(dataframe_1,['col2'])
    
    # Assert
    assert expected == result

def test_1_customer_name_normalised():
    # Assemble
    expected = 5 
    df = extract_file("test_data.csv")
    df = remove_sensitive_data(df,["card_number"])
    # Act
    result = customer_normalised(df)
    
    # Assert 
    assert expected == len(result.index)

@patch("pandas.Series.apply")
def test_2_customer_name_normalised(mock_hash: Mock):
    # Assemble
    data = {'customer_id': [1, 1, 1, 1, 1], 'customer_name': ['Tony', 'Sol','Jose','Candy','Nelly']}
    expected = pd.DataFrame(data=data)
    data_mock = {'customer_id': [1, 1, 1, 1, 1]}
    mock_hash.return_value = pd.DataFrame(data=data_mock)
    df = extract_file("test_data.csv")
    df = remove_sensitive_data(df,["card_number"])
    
    # Act
    result = customer_normalised(df)
    
    # Assert 
    pd_testing.assert_frame_equal(expected,result)

def test_1_payment_type_normalised():
    # Assemble
    expected = 2
    df = extract_file("test_data.csv")
    df = remove_sensitive_data(df,["card_number"])
    # Act
    result = payment_type_normalised(df)
    
    # Assert 
    assert expected == len(result.index)

@patch("pandas.Series.apply")
def test_2_payment_type_normalised(mock_hash: Mock):
    # Assemble
    data = {'payment_type_id': [1, 1], 'payment_type_name': ['CARD', 'CASH']}
    expected = pd.DataFrame(data=data)
    data_mock = {'payment_type_id': [1, 1]}
    mock_hash.return_value = pd.DataFrame(data=data_mock)
    df = extract_file("test_data.csv")
    df = remove_sensitive_data(df,["card_number"])
    
    # Act
    result = payment_type_normalised(df)
    
    # Assert 
    pd_testing.assert_frame_equal(expected,result)

def test_1_product_flavour_normalised():
    # Assemble
    expected = 5
    df = extract_file("test_data.csv")
    df = remove_sensitive_data(df,["card_number"])
    # Act
    result = product_flavour_normalised(df)
    
    # Assert 
    assert expected == len(result.index)

@patch("hashlib.md5")
def test_2_product_flavour_normalised(mock_hash: Mock):
    # Assemble
    data = {'product_flavour_id': ['1', '1', '1', '1', '1'], 'product_flavour_name': ['Hazelnut', 'Caramel', 'NaN','Vanilla','Coffee']}
    expected = pd.DataFrame(data=data)
    expected['product_flavour_id'] = expected['product_flavour_name'].apply(lambda x: hashlib.md5((x.strip()).encode('utf-8')).hexdigest())
    mock_hash.return_value = hashlib.md5('1'.encode('utf-8'))
    df = extract_file("test_data.csv")
    df = remove_sensitive_data(df,["card_number"])
    
    # Act
    result = product_flavour_normalised(df)
    
    # Assert 
    pd_testing.assert_frame_equal(expected,result)

def test_1_product_size_normalised():
    # Assemble
    expected = 2
    df = extract_file("test_data.csv")
    df = remove_sensitive_data(df,["card_number"])
    # Act
    result = product_size_normalised(df)
    
    # Assert 
    assert expected == len(result.index)

@patch("hashlib.md5")
def test_2_product_size_normalised(mock_hash: Mock):
    # Assemble
    data = {'product_size_id': ['1', '1'], 'product_size_name': ['Regular', 'Large']}
    expected = pd.DataFrame(data=data)
    expected['product_size_id'] = expected['product_size_name'].apply(lambda x: hashlib.md5((x.strip()).encode('utf-8')).hexdigest())
    mock_hash.return_value = hashlib.md5('1'.encode('utf-8'))
    df = extract_file("test_data.csv")
    df = remove_sensitive_data(df,["card_number"])
    
    # Act
    result = product_size_normalised(df)
    
    # Assert 
    pd_testing.assert_frame_equal(expected,result)

def test_1_store_normalised():
    # Assemble
    expected = 1
    df = extract_file("test_data.csv")
    df = remove_sensitive_data(df,["card_number"])
    # Act
    result = store_normalised(df)
    
    # Assert 
    assert expected == len(result.index)

@patch("hashlib.md5")
def test_2_store_normalised(mock_hash: Mock):
    # Assemble
    data = {'store_id': ['1'], 'store_name': ['Manchester']}
    expected = pd.DataFrame(data=data)
    expected['store_id'] = expected['store_name'].apply(lambda x: hashlib.md5((x.strip()).encode('utf-8')).hexdigest())
    mock_hash.return_value = hashlib.md5('1'.encode('utf-8'))
    df = extract_file("test_data.csv")
    df = remove_sensitive_data(df,["card_number"])
    
    # Act
    result = store_normalised(df)
    
    # Assert 
    pd_testing.assert_frame_equal(expected,result)

def test_1_orders_normalised():
    # Assemble
    expected = 5
    df = extract_file("test_data.csv")
    df = remove_sensitive_data(df,["card_number"])
    # Act
    result = orders_normalised(df,
                               store_normalised(df),
                               customer_normalised(df),
                               payment_type_normalised(df))
    
    # Assert 
    assert expected == len(result.index)

@patch("hashlib.md5")
def test_2_orders_normalised(mock_hash: Mock):
    # Assemble
    hash_of_1 = hashlib.md5('1'.encode('utf-8')).hexdigest()
    data = {'order_id':         [str(hash_of_1), str(hash_of_1), str(hash_of_1), str(hash_of_1), str(hash_of_1)], 
            'timestamp':        ['21/08/2021 00:00', '22/08/2021 00:00', '23/08/2021 00:00', '24/08/2021 00:00', '25/08/2021 00:00'], 
            'store_id':         [hash_of_1, hash_of_1, hash_of_1, hash_of_1, hash_of_1], 
            'customer_id':      [hash_of_1, hash_of_1, hash_of_1, hash_of_1, hash_of_1], 
            'total_price':      [2.55, 2.55, 2.55, 2.55, 3.10], 
            'payment_type_id':  [hash_of_1, hash_of_1, hash_of_1, hash_of_1, hash_of_1]}
    expected = pd.DataFrame(data=data)
    expected['timestamp'] = expected['timestamp'].apply(lambda x: datetime.datetime.strptime(x,'%d/%m/%Y %H:%M'))
    mock_hash.return_value = hashlib.md5('1'.encode('utf-8'))
    df = extract_file("test_data.csv")
    df = remove_sensitive_data(df,["card_number"])
    
    # Act
    result = orders_normalised(df,
                               store_normalised(df),
                               customer_normalised(df),
                               payment_type_normalised(df))
    
    # Assert 
    pd_testing.assert_frame_equal(expected,result)

def test_1_product_normalised():
    # Assemble
    expected = 5
    df = extract_file("test_data.csv")
    df = remove_sensitive_data(df,["card_number"])
    # Act
    result = product_normalised(df,
                                product_size_normalised(df),
                                product_flavour_normalised(df))
    
    # Assert 
    assert expected == len(result.index)

@patch("hashlib.md5")
def test_2_product_normalised(mock_hash: Mock):
    # Assemble
    hash_of_1 = hashlib.md5('1'.encode('utf-8')).hexdigest()
    data = {'product_id':           [str(hash_of_1), str(hash_of_1), str(hash_of_1)], 
            'product_name':         ['Iced Latte', 'Latte', 'Mocha'], 
            'product_size_id':      [hash_of_1, hash_of_1, hash_of_1], 
            'product_flavour_id':   [hash_of_1, hash_of_1, hash_of_1], 
            'product_price':        [2.55, 2.55, 2.55]}
    expected = pd.DataFrame(data=data)
    mock_hash.return_value = hashlib.md5('1'.encode('utf-8'))
    df = extract_file("test_data.csv")
    df = remove_sensitive_data(df,["card_number"])
    
    # Act
    result = product_normalised(df,
                                product_size_normalised(df),
                                product_flavour_normalised(df))
    
    # Assert 
    pd_testing.assert_frame_equal(expected,result)

def test_1_order_item_normalized():
    # Assemble
    expected = 5
    df = extract_file("test_data.csv")
    df = remove_sensitive_data(df,["card_number"])
    # Act
    result = order_item_normalized(df,
                                   store_normalised(df),
                                   customer_normalised(df),
                                   payment_type_normalised(df),
                                   orders_normalised(df,
                                                     store_normalised(df),
                                                     customer_normalised(df),
                                                     payment_type_normalised(df)),
                                   product_size_normalised(df),
                                   product_flavour_normalised(df),
                                   product_normalised(df,
                                                      product_size_normalised(df),
                                                      product_flavour_normalised(df)))
    
    # Assert 
    assert expected == len(result.index)

@patch("hashlib.md5")
def test_2_order_item_normalized(mock_hash: Mock):
    # Assemble
    hash_of_1 = hashlib.md5('1'.encode('utf-8')).hexdigest()
    data = {'order_id':         [str(hash_of_1)], 
            'product_id':        [str(hash_of_1)], 
            'quantity':         [6], 
            'order_item_id':      [str(hash_of_1)]}
    expected = pd.DataFrame(data=data)
    mock_hash.return_value = hashlib.md5('1'.encode('utf-8'))
    df = extract_file("test_data.csv")
    df = remove_sensitive_data(df,["card_number"])
    
    # Act
    result = order_item_normalized(df,
                                   store_normalised(df),
                                   customer_normalised(df),
                                   payment_type_normalised(df),
                                   orders_normalised(df,
                                                     store_normalised(df),
                                                     customer_normalised(df),
                                                     payment_type_normalised(df)),
                                   product_size_normalised(df),
                                   product_flavour_normalised(df),
                                   product_normalised(df,
                                                      product_size_normalised(df),
                                                      product_flavour_normalised(df)))
    
    # Assert 
    pd_testing.assert_frame_equal(expected,result)

