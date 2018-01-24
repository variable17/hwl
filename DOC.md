# Routes
___
## 0. Hubs - 
#### 1. Get all hubs
* Method - GET
* url - {{url}}/hubs
* Output Json value - 
    ```
    {
    "hubs": [
        {
            "id": 1,
            "name": "office"
        },
        {
            "id": 2,
            "name": "Home"
        }
        ]
    }
    ```
#### 2. Get all the rooms of hub_id
* Method - GET
* url - {{url}}/hubs/<int:id>
* Output Json value - 
    ```
    {
        "hub_id": 2, 
        "hub_name": "Home", 
        "rooms": [
        {
        "id": 1, 
        "name": "Dinning room"
        }
        ]
    }

    ```

#### 3. Add a hub
* Method - POST
* url - {{url}}/hubs
* Input Json value -
    ```
    {
        "name": "Office"
    }
    ```
 


#### 4. Changing a name of a hub
* Method - PUT
* url - {{url}}/hubs/<int:id>
* Input Json value - 
    ```
    {
        "name": "Home"
    }
    ```


#### 5. Delete a hub
* Method - DELETE
* url - {{url}}/hubs/<int:id>
* Output Json value - 
    ```
    msg: Whether operation was successfull or not
    ```
    

___
## 1. Cennets -
#### 1. Get all cennets
* Method - GET
* url - {{url}}/cennets
* Output Json value - 
    ```
            {
        "cennets": [
            {
                "cennet_type": "WALL",
                "discovered": true,
                "id": 1,
                "ip_address": "192.168.1.3",
                "name": "abc",
                "room_id": 1,
                "udid": "HALO"
            }
        ]
    }
    ```

#### 2. Get only one cennet by id
* Method - GET
* url - {{url}}/cennets/<int:id>
* Output Json value - 
    ```
        {
        "cennet_type": "SIDE",
        "dimmers": [
            {
                "id": 1,
                "intensity": 98,
                "number": 1,
                "power": true
            },
            {
                "id": 2,
                "intensity": 0,
                "number": 2,
                "power": false
            }
        ],
        "discovered": true,
        "id": 1,
        "ip_address": "192.168.1.4",
        "name": "def",
        "relays": [
            {
                "id": 1,
                "number": 1,
                "power": true
            },
            {
                "id": 2,
                "number": 2,
                "power": true
            }
        ],
        "room_id": 1,
        "udid": "ADA"
    }
    ```
   
#### 3. Add a cennet
* Method - POST
* url - {{url}}/cennets
* Input Json value - 
    ```
   {
    "udid": "ADA",
    "name": "def",
    "cennet_type": "SIDE",
    "relays" : [{"power":false, "number":1},{"power":false, "number":2}],
    "dimmers": [{"power":false, "intensity":0, "number":1},{"power":false, "intensity":0, "number":2}],
    "ip_address": "192.168.1.4"
    }
    ```
    
#### 4.  Changing the value of room_id in cennet
* Method - PUT
* url - {{url}}/cennets/<int:id>
* Input Json value - 
    ```
    {
    "room_id": 2
    }
    ```
    
#### 5.  Delete a cennet
* Method - DELETE
* url - {{url}}/cennets/<int:id>
* Output Json value - 
    ```
    msg: Whether operation was successfull or not 
    ```
___

## 2. Rooms - 
#### 1. Get all rooms
* Method - GET
* url - {{url}}/rooms
* Output Json value 
    ```
          {
        "rooms": [
            {
                "id": 1,
                "name": "Dinning room"
            }
        ]
    }
    ```
    
#### 2. Get a single room
* Method - GET
* url - {{url}}/rooms/<int:id>
* Output Json value - 
    ```
        {
    "buttons": [
        {
            "button_type": "dimmer",
            "dimmer_id": 1,
            "id": 1,
            "intensity": 98,
            "ip_address": "192.168.1.4",
            "name": "Light",
            "power": true,
            "room_id": 1
        },
        {
            "button_type": "dimmer",
            "dimmer_id": 2,
            "id": 2,
            "intensity": 0,
            "ip_address": "192.168.1.4",
            "name": "Heater",
            "power": false,
            "room_id": 1
        },
        {
            "button_type": "relay",
            "id": 3,
            "ip_address": "192.168.1.4",
            "name": "Fan",
            "power": true,
            "relay_id": 1,
            "room_id": 1
        },
        {
            "button_type": "relay",
            "id": 4,
            "ip_address": "192.168.1.4",
            "name": "Tubelight",
            "power": true,
            "relay_id": 2,
            "room_id": 1
        }
    ],
    "room_id": 1,
    "room_name": "Living Room"
    }
    ```

#### 3. Adding a room
* Method - POST
* url - {{url}}/rooms
* Input Json value - 
    ```
    {
    "name": "Dinning room"
    }
    ```
#### 4. Changing the room name
* Method - PUT
* url - {{url}}/rooms/<int:id>
* Input Json value - 
    ```
    {
        "name": "Living Room"
    }
    ```
     
#### 5. Delete a room
* Method - DELETE
* url - {{url}}/rooms/<int:id>
* Output Json value - 
    ```
    msg: operation succeded or not
    ```
___
## 3. Buttons

#### 1. Get all buttons
* Method - GET
* url - {{url}}/buttons
* Output Json value - 
    ```
        {
        "buttons": [
            {
                "button_type": "dimmer",
                "dimmer_id": 1,
                "id": 1,
                "intensity": 98,
                "ip_address": "192.168.1.4",
                "name": "Light",
                "power": true,
                "room_id": 1
            },
            {
                "button_type": "dimmer",
                "dimmer_id": 2,
                "id": 2,
                "intensity": 0,
                "ip_address": "192.168.1.4",
                "name": "Heater",
                "power": false,
                "room_id": 1
            },
            {
                "button_type": "relay",
                "id": 3,
                "ip_address": "192.168.1.4",
                "name": "Fan",
                "power": true,
                "relay_id": 1,
                "room_id": 1
            },
            {
                "button_type": "relay",
                "id": 4,
                "ip_address": "192.168.1.4",
                "name": "Tubelight",
                "power": true,
                "relay_id": 2,
                "room_id": 1
            }
        ]
    }
    ```

#### 2. Get a single button
* Method - GET
* url - {{url}}/buttons/<int:id>
* Output Json value - 
    ```
   {
    "button_type": "dimmer",
    "dimmer_id": 1,
    "id": 1,
    "intensity": 0,
    "ip_address": "192.168.1.4",
    "name": "Light",
    "power": false,
    "room_id": 1
    }
    ```

#### 3. Add a button
* Method - POST
* url - {{url}}/buttons
* Input Json value - 
    ```
        {
      "name": "Heater",
      "button_type":"dimmer",
      "room_id": 3,
      "ip_address": "192.168.1.4",
      "dimmer_id": 4
    }
    ```
    
#### 4. Change the value of a button
* Method - PUT
* url - {{url}}/buttons/<int:id>
* Input Json value (in case of relay intensity value will not be present) - 
    ```
    {
    "power": false,
    "intensity": 0
    }
    ```

#### 5. Delete a button
* Method - DELETE
* url - {{url}}/buttons/<int:id>
* Output Json value - 
    ```
    msg: operation succedded or not
    ```
    
___

## 4. Register

#### 1. Registering a user
* Method - POST
* url - {{url}}/register
* Input Json value - 
    ```
    {
        "email": "email@email.com",
        "name": "user1",
        "password": "12345"
    }
    ```
    
#### 2. Login a user
* Method - POST
* url - {{url}}/login
* Input Json Value - 
    ```
    {
        "email": "email@email.com",
        "password": "12345"
    }
    ```
* Output Json Value - 
```
    {
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1MTY2MjQxODIsIm5iZiI6MTUxNjYyNDE4MiwianRpIjoiZjUyZWRhZjUtMjc3Yi00MDMwLTk1MjktMjg3MDU0MmRiYjU1IiwiZXhwIjoxNTE2NjI0NDgyLCJpZGVudGl0eSI6ImVtYWlsQGVtYWlsLmNvbSIsImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2VzcyJ9.8rBBF5Fu2YaT-qZ8K3rvDRBThBh9KjnJoIa_BFszsOc",
    "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1MTY2MjQxODIsIm5iZiI6MTUxNjYyNDE4MiwianRpIjoiZGQwYjAxM2QtMThkZC00NWE2LWFhMTAtZTU5NDU1MjFiODk5IiwiZXhwIjoxNTE5MjE2MTgyLCJpZGVudGl0eSI6ImVtYWlsQGVtYWlsLmNvbSIsInR5cGUiOiJyZWZyZXNoIn0.LNzhdPg1IxB3Kbdi6PO20erPj_zdVCAKyay2f6rGFE8"
}
```

#### 3. Accessing a protected url
* Method - GET
* url - {{url}}/protected
* Input Json value - 
    ```
    Authorization header with access token value.
    ```
    
#### 4. Refreshing an access token
* Method - POST
* url - {{url}}/refresh
* Input Json Value - 
    ```
    Authorization header with refresh token value
    ```
* Output Json Value - 
```
{
"access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1MTY2MjQ0NzEsIm5iZiI6MTUxNjYyNDQ3MSwianRpIjoiNjcxN2Q0YzEtNDY0Yy00Yzg0LTkxNTItNTliYzZmMTlmMTQzIiwiZXhwIjoxNTE2NjI0NzcxLCJpZGVudGl0eSI6ImVtYWlsQGVtYWlsLmNvbSIsImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2VzcyJ9.0LGTU0GWfhuSbUZIidljdu9WYz4urQzCvBhA-9YXQZI"
}
```
    
    
    
    
    
    
    
    



