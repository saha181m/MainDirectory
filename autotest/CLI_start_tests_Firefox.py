import pytest
import argparse

parser = argparse.ArgumentParser(description='Start test(s)')
parser.add_argument('-a', '--all', action='store_true', help='Start all tests')
parser.add_argument('-t1', '--test1', action='store_true', help='Start first test - search_dvddom')
parser.add_argument('-t2', '--test2', action='store_true', help='Start second test - auth_dvddom')
parser.add_argument('-t3', '--test3', action='store_true', help='Start second test - adding_to_cart_dvddom')
parser.add_argument('-t4', '--test4', action='store_true', help='Start second test - order_dvddom')
args = parser.parse_args()
if args.all:
    pytest.main(args=['-v', 'search_dvddom.py', 'auth_dvddom.py', 'adding_to_cart_dvddom.py', 'order_dvddom.py'])
elif args.test1:
    pytest.main(args=['-v', 'search_dvddom.py'])
elif args.test2:
    pytest.main(args=['-v', 'auth_dvddom.py'])
elif args.test3:
    pytest.main(args=['-v', 'adding_to_cart_dvddom.py'])
elif args.test4:
    pytest.main(args=['-v', 'order_dvddom.py'])
