import requests
import scripts as scripts_app
from blog import models


class Service:
    def insert_data_from_api(self, api_type:str='all'):
        if api_type:
            pass
        url = scripts_app.POST_API
        response = requests.get(url)
        if response.status_code == 200:            
            datas = response.json()
            object_list = self.make_post_model_paylad(datas)            
            self.bulk_insert(object_list)
    
    def make_post_model_paylad(self, datas):
        object_list = []
        for data in datas:                
            payload = {}
            payload['slug'] = data.get('slug'),
            payload['url'] = data.get('url'),
            payload['title'] = data.get('title'),
            payload['content'] = data.get('content'),
            payload['post_image_url'] = data.get('image'),
            payload['post_thumbnail_url'] = data.get('thumbnail'),
            payload['status'] = data.get('status'),
            payload['category'] = data.get('category')

            object_list.append(payload)
        return object_list


    def bulk_insert(self, datas, chunk_size:int=10):
        # Split the data into smaller chunks
        chunks = [datas[i:i + chunk_size] for i in range(0, len(datas), chunk_size)]

        # Insert objects in chunks
        for chunk in chunks:
            objects_to_insert = [models.Post(**data) for data in chunk]
            models.Post.objects.bulk_create(objects_to_insert)

                   

