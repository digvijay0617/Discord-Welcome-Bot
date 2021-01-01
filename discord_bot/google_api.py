import requests

from settings import settings as settings


class GoogleClient:
    """
    Google client for all google related API calls
    """
    GOOGLE_API_BASE_URL = 'https://www.googleapis.com/customsearch/v1'

    def get_google_search_link(self, query):
        """
        method to return top 5 google search result
        :param query: String
        :return: List
        """
        params = {
            'key': settings.GOOGLE_API_KEY,
            'cx': settings.GOOGLE_ENGINE_ID,
            'q': query,
        }
        try:
            response = requests.get(
                url=self.GOOGLE_API_BASE_URL,
                params=params,
                timeout=settings.REQUEST_TIMEOUT
            ).json()
            results = response.get('items', [])
            top_5_result = []
            for item in results[:5]:
                top_5_result.append(
                    f'{item.get("title")} ---> {item.get("link")}'
                )
            return top_5_result, False
        except Exception as error:
            print(error)
        return [], True
