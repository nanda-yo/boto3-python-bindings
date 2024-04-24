import requests

SERVICE_URL = 'http://0.0.0.0:8181/api/v1/'
#This uses api, u can rearrange some stuff to use db connection directly, it is exposed as itemsdomain.deleteitem()
def delete_bad_items():
    r = requests.get(url = SERVICE_URL+'all')
    xsrf = {'csrftoken': r.cookies.get('csrftoken')}
    hehlist = r.json()
    for item in range(len(hehlist)): #item is r.json()[item]
        if hehlist[item]['sk'] != 'fkr':
            a = requests.delete(url=SERVICE_URL + 'delete?item_pk=' + hehlist[item]['pk'] +'&item_sk='+ hehlist[item]['sk'], headers=xsrf, cookies=xsrf)
            #'http://0.0.0.0:8181/api/v1/delete?item_pk=da1d66b0-a6ae-4d64-893e-2f30999b3ff9&item_sk=Sorting%20Key%2C%20typeof%20str'
            #delete?item_id=6a06e25c-6d23-447d-aec5-740598b6e04f&item_sk=Testing%20sk
            print(a.status_code)
    print('Finished')


if __name__ == "__main__":

    delete_bad_items()