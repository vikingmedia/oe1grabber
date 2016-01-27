oe1grabber
==========

rip and convert "7 Tage Ö1" to mp3

Ö1 is an Austrian radio station, that offers it's program for streaming at http://oe1.orf.at/konsole?show=ondemand. Oe1grabber captures these streams and converts them to mp3 using FFMPEG. The mp3 files can subsequently be downloaded to a mobile device for later consumption.

FORMAT: 1A

# Klassikportal
API draft for Klassikportal project
Version 0.2

# Group Assets
Interacting with assets (= Magento Products)

* no mini objects (products are always transmitted with all fields, thereby eliminating the need for loading detail page)
* all assets are cached in the client and read from cache after initial load in one session
* images are cached in the client as well
* Assets are cached in the API too - cache is only invalidated, when product is updated

## Asset [/assets/{id}{?language}]
A single asset (= Magento Product)

+ Parameters
    + id (required, integer) ... product id of the vod entity 
    + language (string, optional) - language (store_id) 
    	+ default: `de`

+ Attributes (object)
	+ asset_id: 1 (number, required)
	+ asset_type: video (string, required)

### Retrieve an Asset [GET]

+ Response 200 (application/json)
	{
		"asset_id": 1,
		"asset_type": "video",
		"asset_class": "main_program",
		"video_best_quality": "HD",
		"audio_best_quality": "Stereo 2.0",
		"aspect_ratio": "16:9",
		"audio_languages": {
			"de": "Deutsch"
		},
		"subtitle_languages": {
			"de": "Deutsch", 
			"en": "Englisch", 
			"fr": "Französisch", 
			"kr": "Koreanisch"
		},
		"content_rating_fsk": 12,
		"description": "description",
		"description_long": "description_long",
		"description_short": "description_short",
		"duration": 12345.67,
		"genres_main": {
			"docu": "Dokumentarfilm"
		},
		"genres_sub": {
			"makingof": "Making of"
		}
		"copyright": "Unitel (2015)",
		"name": "Bach, Brandenburgisches Konzert Nr. 2 F-Dur BWV 1047",
		"name_supplement": "von den Salzburger Festspielen 2014",
		"production_countries": {
			"de": "Deutschland"
		},
		"production_years": [1992,1993,1994],
		"production_credits": [
			{
				"asset_id": 1234,
				"position": 1,
				"name": "Ivor Bolton",
				"role": "Solist Gesang",
				"part": "Tamino"
			}
		],
		"related_videos": [
		],
		"images": {
			"thumbnail": {
				"192x68": "https://path/to/thumbnail/192x68/image.jpg"
			}
		}
		"content_urls": {
			"web": "https://clsx.org/operas/zauberfloete",
			"ios": "clsx://zauberfloete"
		},
		"chapters": [
			{
				"name": "1. Akt",
				"position": 1,
				"tcin": 0.0,
				"tcout": 302.576
			}
		,
		"epoch": {
			"baroque": "Barock"
		},
		"downloads": [
		]
	}


+ Response 200 (application/json)
	{
		"asset_id": 1,
		"asset_type": "editorial",
		"asset_class": "composer",
		"description": "description",
		"description_long": "description_long",
		"description_short": "description_short",
		"trivia": [
			"Beethovens Vorfahren stammen aus Flandern, daher der Namenszusatz 'von'"
		],
		"works": [
			"9 Symphonien",
			"5 Klavierkonzerte"
		]
		"copyright": "Unitel (2015)",
		"name": "Johann Sebastian Bach",
		"name_supplement": "Komponist, 1831 - 1897",
		"images": {
			"thumbnail": {
				"192x68": "https://path/to/thumbnail/192x68/image.jpg"
			}
		}
		"content_urls": {
			"web": "https://clsx.org/composers/johann-sebastian-bach",
			"ios": "clsx://editorial/1234"
		},
		"epoch": {
			"baroque": "Barock"
		},
		"instrument": null,
		"voice_type": null,
		"related_videos": [
		],
		"downloads": [
		]
	}


## Assets [/assets{?limit,sort,dir,page,language,asset_type,asset_class}]
Get a list of assets (= Magento Products) 
*Note:* Use the filters API to performantely retrieve lists of assets

+ Parameters
	+ limit (number, optional) - the maximum number of results to return
		+ default: `25`
	+ sort (string, optional) - datafield for sorting
		+ default: `name`
	+ dir (string, optional) - sort direction (`asc` or `desc`)
		+ default: `asc`
	+ page (number, optional) - page number to show (pages are `limit` long), numbering starts with `1` (there is no page `0`)
		+ default: `1`
	+ language (string, optional) - store_id
		+ default: `de`
	+ asset_type (string, optional) - list of desired asset types (= Magento attribute_set), e.g. asset_type=video,editorial
		+ default: `all`
	+ asset_class (string, optional) - list of asset_classes (e.g. video assets: "main", "supplemental", editorials: "director", "orchestra", "festival")
		+ default: `all`

### Retrive Assets [GET]

+ Response 200 (application/json)
	{	"assets": 
		[
			{
				"asset_id": 1,
				"asset_type": "video",
				"asset_class": "main_program",
				"video_best_quality": "HD",
				"audio_best_quality": "Stereo 2.0",
				"aspect_ratio": "16:9",
				"audio_languages": {
					"de": "Deutsch"
				},
				"subtitle_languages": {
					"de": "Deutsch", 
					"en": "Englisch", 
					"fr": "Französisch", 
					"kr": "Koreanisch"
				},
				"content_rating_fsk": 12,
				"description": "description",
				"description_long": "description_long",
				"description_short": "description_short",
				"duration": 12345.67,
				"genres_main": {
					"docu": "Dokumentarfilm"
				},
				"genres_sub": {
					"makingof": "Making of"
				}
				"copyright": "Unitel (2015)",
				"name": "Bach, Brandenburgisches Konzert Nr. 2 F-Dur BWV 1047",
				"name_supplement": "von den Salzburger Festspielen 2014",
				"production_countries": {
					"de": "Deutschland"
				},
				"production_years": [1992,1993,1994],
				"production_credits": [
					{
						"asset_id": 1234,
						"position": 1,
						"name": "Ivor Bolton",
						"role": "Solist Gesang",
						"part": "Tamino"
					}
				],
				"related_videos": [
				],
				"images": {
					"thumbnail": {
						"192x68": "https://path/to/thumbnail/192x68/image.jpg"
					}
				}
				"content_urls": {
					"web": "https://clsx.org/operas/zauberfloete",
					"ios": "clsx://zauberfloete"
				},
				"chapters": [
					{
						"name": "1. Akt",
						"position": 1,
						"tcin": 0.0,
						"tcout": 302.576
					}
				],
				"epoch": {
					"baroque": "Barock"
				},
				"downloads": [
				]
			}
		]
	}

## Videos [/videos/{asset_id}]

+ Request (application/json)
	+ Body
		{
		}

+ Response 200 (application/dash+xml)

+ Response 200 (application/vnd.apple.mpegurl)

+ Response 403 (application/json)
	+ Body
		{
			"error": {
				"message": "Bitte melden Sie sich an, um dieses Video anzusehen!"
			}
		}


# Group Filter

## Filters [/filters]

### Get Filters [GET]

+ Attributes(object)
	+ category_id: category_id (required, string) - Category to filter

+ Response 200 (application/json)
	{
		"assets": {

		},
		"filters": [
			{
				"name": "Genres",
				"request_var": "genres",
				"items": [
					{"value": 249, "label": "Animation"}
				]
			}
		],
		"filters_active": [
			{
				"name": "Genres",
				"request_var": "genres",
				"items": [
					{"value": 249, "label": "Animation"}
				]
			}
		]
	}


# Group Relations
User / Asset relations, like bookmarks, watchlist, etc.

## Relations [/relations{?append,limit,sort,dir,page,relation_type}]
Handle User / Asset relations like bookmarkin, watchlist and ratings - may also trigger nCanto events.

+ Parameters
	+ user_id: user_id (required, number)
	+ append: appendable_objects (optional, string) - e.g. assets
	+ limit (number, optional) - the maximum number of results to return
		+ default: `25`
	+ sort (string, optional) - datafield for sorting
		+ default: `name`
	+ dir (string, optional) - sort direction (`asc` or `desc`)
		+ default: `asc`
	+ page (number, optional) - page number to show (pages are `limit` long), numbering starts with `1` (there is no page `0`)
		+ default: `1`
	+ relation_type (string, optional) - list of desired relation types, e.g. relation_type=bookmarked,watched
		+ default: `all`


### Retrieve Relations [GET]

+ Parameters
	+ user_id: user_id (required, number)
	+ asset_id: asset_id (number, optional) - restrict result to one asset


+ Request (application/json)
	+ Body
		{
			"user_id": 1234,
			"asset_id": 1
		}


+ Response 200 (application/json)
	+ Body
		{
			"relations": 
			[
				{
					"asset_id": 5678,
					"visited": 1452790531,
					"bookmarked": 1452790531,
					"playback_position": 359.456
					"watched": 1452790531,
					"rating": 0.0,	
					"rated": 1452790531
				},
				{
					"asset_id": 5678,
					"visited": 1452790531,
					"bookmarked": 1452790531,
					"playback_position": 359.456
					"watched": 1452790531,
					"rating": 0.0,	
					"rated": 1452790531
				}
			],
			"assets": [
			]
		}

### Set Relations [POST]

+ Request (application/json)
	+ Body
		{
			"user_id": 1234,
			"bookmarked": [
				{
					"asset_id": 5678
				}
			],
			"watched": [
				{
					"asset_id": 5678
				}
			],
			"rated": [
				{
					"asset_id": 5678,
					"rating": 1.0
				}
			],
			"visited": [
				{
					"asset_id": 5678
				}
			]
		}

+ Response 200 (application/json)
	+ Body
		{
			"relations": 
			[
				{
					"asset_id": 5678,
					"visited": 1452790531,
					"bookmarked": 1452790531,
					"playback_position": 359.456
					"watched": 1452790531,
					"rating": 0.0,	
					"rated": 1452790531
				},
				{
					"asset_id": 5678,
					"visited": 1452790531,
					"bookmarked": 1452790531,
					"playback_position": 359.456
					"watched": 1452790531,
					"rating": 0.0,	
					"rated": 1452790531
				}
			],
			"assets": [
			]
		}


#### Delete Relations [DELETE]
Delete User / Asset relations. Deleting `rating` results in resetting the rating to 0.0. 

+ Request (application/json)
	+ Body
		{
			"user_id": 1234,
			"bookmarked": [
				{
					"asset_id": 5678
				}
			],
			"watched": [
				{
					"asset_id": 5678
				}
			],
			"rated": [
				{
					"asset_id": 5678,
				}
			],
			"visited": [
				{
					"asset_id": 5678
				}
			]
		}


# Group Users

## Log In [/login]
Log in a user and open a new session

### Log in [POST]

+ Request (application/json)
	+ Body
		{
			"username": "erik@flimmit.com",
			"password": "123456"
		}

+ Response 200 (application/json)
    + Header
            sid: session_id

	+ Body
		{
			"user_id": 1234,
			"email": "erik@flimmit.com",
			"prefix": "Herr",
			"firstname": "Erik",
			"lastname": "Seethaler"
		}

### Log out [DELETE]

+ Request (application/json)

+ Response 200 (application/json)


## User [/users/{user_id}]


# Group Eventlogs
Eventlogs are used for 

* help debugging
* help the support team to retrace problems
* determine the assets share of subscription revenue
* QoS (dropped frames, stalls etc.)

## Eventlogs [/eventlogs]

### Send Events [POST]

+ Request (application/json)
	+ Body
		{	
			"events": [
				{
					"user_id": 1234,
					"asset_id": 5678,
					"player_session_id": "a8098c1a-f86e-11da-bd1a-00112444be1e",
					"event_audit_number": 1,
					"event_type": "ui",
					"event_class": "pause",
					"player_state": "playing"
					"event_time": 1453206150,
					"event_data": {
						"ui_element": "pause_button",
						"ui_action": "click",
					}
				},
				{
					"user_id": 1234,
					"asset_id": 5678,
					"player_session_id": "a8098c1a-f86e-11da-bd1a-00112444be1e",
					"event_audit_number": 2,
					"event_type": "player",
					"event_class": "mute",
					"player_state": "playing"
					"event_time": 1453206150,
					"event_data": {
						"mute": False
					}
				}
			]
		}

+ Response 204 (application/json)

# Group Recommendations and Lists

## Recommendations [/recommendations{?append,limit,sort,dir,page,context}]

### Get Recommendations [GET]

+ Parameters
	+ user_id: user_id (required, number)
	+ context (string, required) - nCanto context, specifies the kind of recommendation
	+ asset_id: asset_id (optional, number)
	+ append: appendable_objects (optional, string) - e.g. assets
	+ limit (number, optional) - the maximum number of results to return
		+ default: `25`
	+ sort (string, optional) - datafield for sorting
		+ default: `name`
	+ dir (string, optional) - sort direction (`asc` or `desc`)
		+ default: `asc`
	+ page (number, optional) - page number to show (pages are `limit` long), numbering starts with `1` (there is no page `0`)
		+ default: `1`

		
+ Request (application/json)
	+ Body
		{
			"user_id": 1234,
			"asset_id": 5678,
			"context": "similar_items_of_same_kind"
		}

+ Response 200 (application/json)
	+ Body
		{
			"recommendations": 
			[
				{
					"asset_id": 1214,
					"score": 0.53421
				}
			]
		}


## Lists [/lists{?append,limit,sort,dir,page,list_ids}]
Statistically calculated lists
Available Lists:

* bestRated8h (best rated assets in the last 8 hours)
* hottest3d (hottest assets of the last 3 days)
* bestRated1w (best rated 1 week)
* mostWatched8h (most watched 8 hours)
* bestRated1d (best rated 1 day)
* mostPopular1d (most popular 1 day)
* hottest12h (hottest 12 hours)
* mostShared8h (most shared 8 hours)
* mostPopular8h (most popular 8 hours)
* mostShared1d (most shared 1 day)
* mostPopular1w (most popular 1 week)
* hottest4h (hottest 4 hours)
* mostWatched1d (most watched 1 day)
* mostWatched1w (most watched 1 week)
* mostShared1w (most shared 1 week)

### Get lists [GET]

+ Parameters
	+ append: appendable_objects (optional, string) - e.g. assets
	+ limit (number, optional) - the maximum number of results to return
		+ default: `25`
	+ sort (string, optional) - datafield for sorting
		+ default: `name`
	+ dir (string, optional) - sort direction (`asc` or `desc`)
		+ default: `asc`
	+ page (number, optional) - page number to show (pages are `limit` long), numbering starts with `1` (there is no page `0`)
		+ default: `1`
	+ list_ids (string, required) - lists to retrieve, e.g. list_ids=mostPopular1w,mostWatched1w
		+ default: `all`

+ Response 200 (application/json)
	+ Body
		{
			"lists":
			{
				"mostPopular1w": 
				[
					{
						"asset_id": 1234,
						"score": 0.75
					}
				]
			}
		}


# Group Search & Filtering

## Search Suggest [/suggests]

### Get Suggestions [GET]

+ Attributes(object)
	+ q: query (required, string) - Query to get suggestions for, e.g. "anna"
	+ limit: maximum_result_number (optional, number) - desired max. number of results, defaults to 5

+ Response 200 (application/json)
	{
		"q": "anna",
		"results": [
			{
				"name": "Anna Netrebko",
				"info": "Opernsängerin (Sopran)",
				"thumbnail": "https://en.wikipedia.org/wiki/File:Anna_Netrebko_-_Romy_2013_a.jpg",
				"alias": "/solists/anna-netrebko",
				"asset_id": 1234
			},
			{
				"name": "Rolando Villazón",
				"info": "Opernsänger (Tenor)",
				"thumbnail": "http://www.wheremilan.com/wp-content/uploads/2014/04/Riccardo_Villazon.jpg",
			},
		] 
	}

## Full Text Search [/search]

### Get Search Result [GET]

+ Attributes(object)
	+ q: query (required, string) - Query to search for, e.g. "anna"

+ Response 200 (application/json)
	{
		"q": "anna",
		"results": [
		] 
	}



# Misc

## App Version [/appversion]

For the forced update feature

### Get App Verision [GET]

+ Response 200 (application/json)
	{
		"android": {
			"current_version": "1.0.0",
			"version": "2.0.0",
			"minimum_os_version": "7.0.0"
		},
		"ios": {
			"version": "2.0.0",
			"minimum_os_version": "7.0.0"	
		}
	}

# Data Structures
