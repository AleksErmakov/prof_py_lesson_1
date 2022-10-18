from application.salary import calculate_salary
from application.db.people import get_employess
from datetime import date
from for_pandas import func_pandas

if __name__ == '__main__':

    print(date.today())
    calculate_salary(10)
    get_employess('Aleks')
    func_pandas()

