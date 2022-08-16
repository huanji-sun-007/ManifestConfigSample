// config edgeAgent
config.ModulesContent.Add("$edgeAgent",
    new Dictionary<string, object>
    {
        ["properties.desired"] = new
        {
            schemaVersion = "1.1",
            runtime = new
            {
                type = "docker",
                settings = new
                {
                    loggingOptions = string.Empty,
                    minDockerVersion = "v1.25",
                    registryCredentials = new Dictionary<string, Dictionary<string, string>>() {
                {
                    "name", new Dictionary<string, string>()
                    {
                        { "address", "dummyAddress" },
                        { "username", "dummyUsername" },
                        { "password", "dummyPassword" },
                    }
                }
            },
                },
            },

            systemModules = new
            {
                edgeAgent = new
                {
                    type = "docker",
                    settings = new
                    {
                        image = $"mcr.microsoft.com/azureiotedge-agent:1.1",
                        createOptions = string.Empty,
                    },
                },
                edgeHub = new
                {
                    type = "docker",
                    status = "running",
                    restartPolicy = "always",
                    settings = new
                    {
                        image = $"mcr.microsoft.com/azureiotedge-hub:1.1",
                        createOptions = "{\"HostConfig\":{\"PortBindings\":{\"443/tcp\":[{\"HostPort\":\"443\"}],\"5671/tcp\":[{\"HostPort\":\"5671\"}],\"8883/tcp\":[{\"HostPort\":\"8883\"}]}}}",
                    },
                },
            },
            modules = new Dictionary<string, object>()
            {
                {
                    "moduleName", new 
                    {
                        version = "1.1",
                        type = "docker",
                        status = "running",
                        restartPolicy = "always",
                        settings = new 
                        {
                            image = "imageUri",
                            createOptions = "",
                        },
                        env = new Dictionary<string, string>()
                        {
                            {"Key", "Value" }
                        },
                    }
                }
            },
        },
    });

// Config edgeHub
config.ModulesContent.Add("$edgeHub",
    new Dictionary<string, object>
    {
        ["properties.desired"] = new
        {
            schemaVersion = edgeHubDesiredProperties.SchemaVersion,
            routes = new Dictionary<string, string>()
            {
                {"routeName", "route" },
            },
            storeAndForwardConfiguration = new
            {
                timeToLiveSecs = 7200,
            },
        },
    });

// Config Custom Module
config.ModulesContent.Add("CustomModule", 
    new Dictionary<string, object>
    {
        ["properties.desired"] = new 
        { 
            customObject = "custom properties" 
        },
    });