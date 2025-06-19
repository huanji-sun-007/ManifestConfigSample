#!/usr/bin/env python3
"""
Azure IoT Edge Manifest Configuration Sample in Python
This is a Python equivalent of the Sample.cs file for configuring Azure IoT Edge modules.
"""

import json

# Initialize the configuration structure
config = {
    "modulesContent": {}
}

# Assuming edgeHubDesiredProperties has a SchemaVersion property
# This would typically come from another part of the application
edgeHubDesiredProperties = {
    "SchemaVersion": "1.2"
}

# Config edgeAgent
config["modulesContent"]["$edgeAgent"] = {
    "properties.desired": {
        "schemaVersion": "1.1",
        "runtime": {
            "type": "docker",
            "settings": {
                "loggingOptions": "",
                "minDockerVersion": "v1.25",
                "registryCredentials": {
                    "name": {
                        "address": "dummyAddress",
                        "username": "dummyUsername",
                        "password": "dummyPassword"
                    }
                }
            }
        },
        "systemModules": {
            "edgeAgent": {
                "type": "docker",
                "settings": {
                    "image": "mcr.microsoft.com/azureiotedge-agent:1.1",
                    "createOptions": ""
                }
            },
            "edgeHub": {
                "type": "docker",
                "status": "running",
                "restartPolicy": "always",
                "settings": {
                    "image": "mcr.microsoft.com/azureiotedge-hub:1.1",
                    "createOptions": json.dumps({
                        "HostConfig": {
                            "PortBindings": {
                                "443/tcp": [{"HostPort": "443"}],
                                "5671/tcp": [{"HostPort": "5671"}],
                                "8883/tcp": [{"HostPort": "8883"}]
                            }
                        }
                    })
                }
            }
        },
        "modules": {
            "moduleName": {
                "version": "1.1",
                "type": "docker",
                "status": "running",
                "restartPolicy": "always",
                "settings": {
                    "image": "imageUri",
                    "createOptions": ""
                },
                "env": {
                    "Key": "Value"
                }
            }
        }
    }
}

# Config edgeHub
config["modulesContent"]["$edgeHub"] = {
    "properties.desired": {
        "schemaVersion": edgeHubDesiredProperties["SchemaVersion"],
        "routes": {
            "routeName": "route"
        },
        "storeAndForwardConfiguration": {
            "timeToLiveSecs": 7200
        }
    }
}

# Config Custom Module
config["modulesContent"]["CustomModule"] = {
    "properties.desired": {
        "customObject": "custom properties"
    }
}

# Example usage - print the configuration as JSON
if __name__ == "__main__":
    print("Azure IoT Edge Manifest Configuration:")
    print(json.dumps(config, indent=2))