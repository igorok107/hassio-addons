# Home Assistant Add-on: HTTP to MQTT

A Home Assistant addon for publish the HTTP request data via MQTT.

## Installation

Add the repository URL under **Supervisor → Add-on store → ⋮ → Manage add-on repositories**:

    https://github.com/igorok107/hassio_addons

Then search for `HTTP to MQTT` and install it.

## Configuration

Example add-on configuration:

```yaml
mqtt_host: 192.168.1.100
mqtt_port: 1883
mqtt_user: mqtt_user
mqtt_password: mqtt_pass
```

### Option: `mqtt_host`

The `mqtt_host` option is the ip address of your mqtt server. If you are using the embeded server in Home Assistant just use your instances ip address or mqtt://core-mosquitto.

### Option: `mqtt_user`

This is the username required to access your mqtt server.

### Option: `mqtt_password`

The password of the mqtt user account.

## Known issues and limitations

- This add-on is totally beta. 
