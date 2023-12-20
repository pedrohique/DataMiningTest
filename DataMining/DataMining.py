import requests
import time
from random import randint
import re

class DataMining:
    def __init__(self, busca, qtd_pags):
        self.busca = busca
        self.qtd_pags = qtd_pags
        self.tweets_dict = {}
        self.id_tweets = []
        self.tweets_list = []
        self.busca_tweets()

    def __call__(self, *args, **kwargs):
        return tuple(self.tweets_list)

    def __iter__(self):
        tweet_tuple = tuple(self.tweets_list)
        for i in tweet_tuple:
            yield i

    def __len__(self):
        return len(self.tweets_list)

    def busca_tweets(self):
        headers = {
            'authority': 'twitter.com',
            'accept': '*/*',
            'accept-language': 'pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
            'content-type': 'application/json',
            'cookie': '_ga=GA1.2.919975865.1685405380; g_state={"i_l":1,"i_p":1685412604086}; kdt=EyQ2RMbBzKN408uUDq3eBcyz8GNvkmcJ2OCcGDOT; _gid=GA1.2.1736674757.1700417087; auth_multi="1194699488629272577:7e93447c8fa24c412c272c5e15fcc68b4a9e44e2"; auth_token=96b91a0bc136ba50c618e0273e6d3e29137807d2; guest_id_ads=v1%3A170042202239197568; guest_id_marketing=v1%3A170042202239197568; guest_id=v1%3A170042202239197568; twid=u%3D95677431; ct0=78d48a379a78256fadd63993a65c6af8860815af7329c6d64dfc27693e631bb953020f74e42ab295ac3d71d9bc6529e2631e30384f8b8c8006fb2ad9249bdd746313ab8cb9e7cb479100628eb83b6f2f; lang=pt; personalization_id="v1_CaVWztBdtJ16f1bJVLnv1A=="',
            'referer': 'https://twitter.com/search?q='+self.busca+'&src=typed_query&f=top',
            'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
            'x-client-transaction-id': 'R+mt+WHTWkz641rCXt+mAL9Kgdtyhao9wS2hJw0TymSWGzrOr+vTbx7tY2/tD/+WaXpqS0ZCp7sxrevCfSIB/zc8xyYmRg',
            'x-client-uuid': '97a6aa50-ef5e-465f-a4d4-b7afa4c6532e',
            'x-csrf-token': '78d48a379a78256fadd63993a65c6af8860815af7329c6d64dfc27693e631bb953020f74e42ab295ac3d71d9bc6529e2631e30384f8b8c8006fb2ad9249bdd746313ab8cb9e7cb479100628eb83b6f2f',
            'x-twitter-active-user': 'yes',
            'x-twitter-auth-type': 'OAuth2Session',
            'x-twitter-client-language': 'pt',
        }
        cursor_atual = ''
        for page in range(self.qtd_pags):
            print(page)

            params = (
                ('variables',
                 '{"rawQuery":"' + self.busca + '","count":20,"querySource":"typed_query","product":"Top"}'),
                ('features',
                 '{"responsive_web_graphql_exclude_directive_enabled":true,"verified_phone_label_enabled":false,"responsive_web_home_pinned_timelines_enabled":true,"creator_subscriptions_tweet_preview_api_enabled":true,"responsive_web_graphql_timeline_navigation_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"c9s_tweet_anatomy_moderator_badge_enabled":true,"tweetypie_unmention_optimization_enabled":true,"responsive_web_edit_tweet_api_enabled":true,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,"view_counts_everywhere_api_enabled":true,"longform_notetweets_consumption_enabled":true,"responsive_web_twitter_article_tweet_consumption_enabled":false,"tweet_awards_web_tipping_enabled":false,"freedom_of_speech_not_reach_fetch_enabled":true,"standardized_nudges_misinfo":true,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":true,"longform_notetweets_rich_text_read_enabled":true,"longform_notetweets_inline_media_enabled":true,"responsive_web_media_download_video_enabled":false,"responsive_web_enhance_cards_enabled":false}'),
            )
            if page > 0:
                if cursor_atual:
                    params = (
                        ('variables', '{"rawQuery":"'+self.busca+'","count":20,"cursor":"'+cursor_atual+'","querySource":"typed_query","product":"Top"}'),
                        ('features',
                         '{"responsive_web_graphql_exclude_directive_enabled":true,"verified_phone_label_enabled":false,"responsive_web_home_pinned_timelines_enabled":true,"creator_subscriptions_tweet_preview_api_enabled":true,"responsive_web_graphql_timeline_navigation_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"c9s_tweet_anatomy_moderator_badge_enabled":true,"tweetypie_unmention_optimization_enabled":true,"responsive_web_edit_tweet_api_enabled":true,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,"view_counts_everywhere_api_enabled":true,"longform_notetweets_consumption_enabled":true,"responsive_web_twitter_article_tweet_consumption_enabled":false,"tweet_awards_web_tipping_enabled":false,"freedom_of_speech_not_reach_fetch_enabled":true,"standardized_nudges_misinfo":true,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":true,"longform_notetweets_rich_text_read_enabled":true,"longform_notetweets_inline_media_enabled":true,"responsive_web_media_download_video_enabled":false,"responsive_web_enhance_cards_enabled":false}'),
                    )


            response = requests.get('https://twitter.com/i/api/graphql/lZ0GCEojmtQfiUQa5oJSEw/SearchTimeline',
                                    headers=headers, params=params)

            if response.status_code == 200:
                resp_json = response.json()

                data = resp_json.get('data', {}).get('search_by_raw_query',{}).get('search_timeline', {}).get('timeline', {}).get('instructions', {})[0].get('entries', {})


                for tweet in data:
                    if tweet.get('entryId', '').startswith('tweet-'):
                        # print(tweet.get('entryId', ''))
                        id = tweet.get('entryId', '').split('-')[1]
                        result = tweet.get('content', {}).get('itemContent', {}).get('tweet_results', {}).get('result', {})

                        user_data = self.get_user_data(result)
                        comment_data = self.get_tweet_data(result)

                        data_clean = self.care_data(user_data, comment_data)



                        if id not in self.id_tweets:
                            if data_clean:
                                self.tweets_list.append(data_clean[id])
                                self.id_tweets.append(id)

                    elif tweet.get('entryId', '').startswith('cursor-top-') or tweet.get('entryId', '').startswith('cursor-bottom') :
                        cursor = tweet.get("content", '').get('value', '')
                        if cursor_atual != cursor:
                            cursor_atual = cursor

                    elif len(resp_json.get('data', {}).get('search_by_raw_query',{}).get('search_timeline', {}).get('timeline', {}).get('instructions', {})) >= 3:
                        cursor2 = resp_json.get('data', {}).get('search_by_raw_query',{}).get('search_timeline', {}).get('timeline', {}).get('instructions', {})[2].get('entry', {}).get("content", {}).get("value", '')
                        if cursor_atual != cursor2:
                            cursor_atual = cursor2

            timer = randint(1, 10)
            print(f'Aguardando {timer} segundos para proxima pagina')
            print(len(self.tweets_list))
            time.sleep(timer)

    def get_user_data(self, tweet):
        user_data = {}
        tweet = tweet.get("core", {}).get("user_results", {}).get("result", {})
        print(tweet)
        keys_legacy = ('created_at', 'default_profile', 'default_profile_image', 'description', 'fast_followers_count',
                       'favourites_count', 'followers_count', 'location', 'name', 'normal_followers_count',
                       'possibly_sensitive', 'screen_name', 'verified', 'professional')
        is_blue_verified = tweet.get('is_blue_verified', '')
        rest_id = tweet.get("rest_id", '')
        legacy = tweet.get("legacy", '')
        if legacy:
            user_data[rest_id] = {}
            user_data[rest_id]['is_blue_verified'] = is_blue_verified
            for key in keys_legacy:
                if key == 'description':
                    legacy[key] = legacy.get(key, '').rstrip().replace('  ', ' ').replace('\n', ' ').replace('  ', ' ').replace('  ', ' ')
                user_data[rest_id][key] = legacy.get(key, '')


        return user_data

    def get_tweet_data(self, tweet):
        keys_tweet = ("created_at", "conversation_id_str", "full_text",
                      "possibly_sensitive", "reply_count", "retweet_count", "favorite_count")
        tweet_data = {}
        rest_id = tweet.get("rest_id", '')
        views = tweet.get("views", {}).get("count", '')

        legacy = tweet.get("legacy", {})
        if legacy:
            self.trata_midia(legacy, tweet_data)
            tweet_data[rest_id] = {}
            tweet_data[rest_id]['id_tweet'] = rest_id
            tweet_data[rest_id]['views'] = views
            for key in keys_tweet:
                if key =='full_text':
                    legacy[key] = legacy.get(key, '').rstrip().replace('  ', ' ').replace('\n', ' ')


                tweet_data[rest_id][key] = legacy.get(key, '')



        return tweet_data

    def trata_midia(self, legacy, tweet_data):
        midia_keys = ("type", "url", "video_info", "media_url_https")
        midias = legacy.get("entities", {}).get("media", [])
        # if midias:
        #     print('---------------------------------------')
        #     for midia in midias:
        #         for key in midia_keys:
        #             print(key, ': ', midia.get(key))
        #
        #     print('---------------------------------------')

    def care_data(self, user_data, comment_data):
        for id in comment_data.keys():
            user_id = user_data.keys()
            for key in user_id:
                for keys in user_data.get(key, {}):
                    comment_data[id][keys] = user_data.get(key, {}).get(keys, '')

        return comment_data
