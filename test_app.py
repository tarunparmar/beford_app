import pytest
import functions 
import pandas as pd 
from pandas.testing import assert_frame_equal
from mock import MagicMock

TEST_DF = pd.DataFrame({
    'Actual Count':[230,124,97,70,64,54,40,54,38],
    'Expected Count':[232,136,96,75,61,52,45,39,35]
})

@pytest.fixture
def mock_figure(mocker):
    return mocker.patch('plotly.graph_objs._figure.Figure',return_value=MagicMock())

@pytest.mark.runthis 
def test_chi_sq():
    '''Test Chi Sq'''
    assert functions.chi_square_test(TEST_DF["Actual Count"], TEST_DF["Expected Count"]) == 8.226208151180925

@pytest.mark.runthis 
def test_benford(mock_figure):
    '''Test Benford'''
    expdf = pd.DataFrame({'Benford':[30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6] , 
                           'Number':[1,2,3,4,5,6,7,8,9],
                            'Actual Count': [2,2,0,0,0,0,0,0,0],
                            'Frequency': [0.5,0.5,0,0,0,0,0,0,0],
                            'Expected Count': [1,1,0,0,0,0,0,0,0]})
    _, df = functions.benfords(pd.DataFrame({'A':[0,1,10,2,20]}))
    assert_frame_equal(df, expdf)



    # pytest -s -m runthis