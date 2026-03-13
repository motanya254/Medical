## GitHub Copilot Chat

- Extension: 0.37.9 (prod)
- VS Code: 1.109.4 (c3a26841a84f20dfe0850d0a5a9bd01da4f003ea)
- OS: linux 6.14.0-29-generic x64
- GitHub Account: mitchelle-cloud

## Network

User Settings:
```json
  "http.systemCertificatesNode": true,
  "github.copilot.advanced.debug.useElectronFetcher": true,
  "github.copilot.advanced.debug.useNodeFetcher": false,
  "github.copilot.advanced.debug.useNodeFetchFetcher": true
```

Connecting to https://api.github.com:
- DNS ipv4 Lookup: Error (0 ms): getaddrinfo ENOTFOUND api.github.com
- DNS ipv6 Lookup: Error (1 ms): getaddrinfo ENOTFOUND api.github.com
- Proxy URL: None (0 ms)
- Electron fetch (configured): Error (2 ms): Error: net::ERR_NAME_NOT_RESOLVED
	at SimpleURLLoaderWrapper.<anonymous> (node:electron/js2c/utility_init:2:10684)
	at SimpleURLLoaderWrapper.emit (node:events:519:28)
  [object Object]
  {"is_request_error":true,"network_process_crashed":false}
- Node.js https: Error (19 ms): Error: getaddrinfo ENOTFOUND api.github.com
	at GetAddrInfoReqWrap.onlookupall [as oncomplete] (node:dns:122:26)
- Node.js fetch: Error (29 ms): TypeError: fetch failed
	at node:internal/deps/undici/undici:14900:13
	at process.processTicksAndRejections (node:internal/process/task_queues:105:5)
	at async n._fetch (/home/emobilis/.vscode/extensions/github.copilot-chat-0.37.9/dist/extension.js:4862:26129)
	at async n.fetch (/home/emobilis/.vscode/extensions/github.copilot-chat-0.37.9/dist/extension.js:4862:25777)
	at async u (/home/emobilis/.vscode/extensions/github.copilot-chat-0.37.9/dist/extension.js:4894:190)
	at async CA.h (file:///usr/share/code/resources/app/out/vs/workbench/api/node/extensionHostProcess.js:116:41743)
  Error: getaddrinfo ENOTFOUND api.github.com
  	at GetAddrInfoReqWrap.onlookupall [as oncomplete] (node:dns:122:26)

Connecting to https://api.githubcopilot.com/_ping:
- DNS ipv4 Lookup: Error (1 ms): getaddrinfo ENOTFOUND api.githubcopilot.com
- DNS ipv6 Lookup: Error (0 ms): getaddrinfo ENOTFOUND api.githubcopilot.com
- Proxy URL: None (0 ms)
- Electron fetch (configured): Error (2 ms): Error: net::ERR_NAME_NOT_RESOLVED
	at SimpleURLLoaderWrapper.<anonymous> (node:electron/js2c/utility_init:2:10684)
	at SimpleURLLoaderWrapper.emit (node:events:519:28)
  [object Object]
  {"is_request_error":true,"network_process_crashed":false}
- Node.js https: Error (20 ms): Error: getaddrinfo ENOTFOUND api.githubcopilot.com
	at GetAddrInfoReqWrap.onlookupall [as oncomplete] (node:dns:122:26)
- Node.js fetch: Error (23 ms): TypeError: fetch failed
	at node:internal/deps/undici/undici:14900:13
	at process.processTicksAndRejections (node:internal/process/task_queues:105:5)
	at async n._fetch (/home/emobilis/.vscode/extensions/github.copilot-chat-0.37.9/dist/extension.js:4862:26129)
	at async n.fetch (/home/emobilis/.vscode/extensions/github.copilot-chat-0.37.9/dist/extension.js:4862:25777)
	at async u (/home/emobilis/.vscode/extensions/github.copilot-chat-0.37.9/dist/extension.js:4894:190)
	at async CA.h (file:///usr/share/code/resources/app/out/vs/workbench/api/node/extensionHostProcess.js:116:41743)
  Error: getaddrinfo ENOTFOUND api.githubcopilot.com
  	at GetAddrInfoReqWrap.onlookupall [as oncomplete] (node:dns:122:26)

Connecting to https://copilot-proxy.githubusercontent.com/_ping:
- DNS ipv4 Lookup: Error (0 ms): getaddrinfo ENOTFOUND copilot-proxy.githubusercontent.com
- DNS ipv6 Lookup: Error (0 ms): getaddrinfo ENOTFOUND copilot-proxy.githubusercontent.com
- Proxy URL: None (0 ms)
- Electron fetch (configured): Error (13 ms): Error: net::ERR_NAME_NOT_RESOLVED
	at SimpleURLLoaderWrapper.<anonymous> (node:electron/js2c/utility_init:2:10684)
	at SimpleURLLoaderWrapper.emit (node:events:519:28)
  [object Object]
  {"is_request_error":true,"network_process_crashed":false}
- Node.js https: Error (43 ms): Error: getaddrinfo ENOTFOUND copilot-proxy.githubusercontent.com
	at GetAddrInfoReqWrap.onlookupall [as oncomplete] (node:dns:122:26)
- Node.js fetch: Error (25 ms): TypeError: fetch failed
	at node:internal/deps/undici/undici:14900:13
	at process.processTicksAndRejections (node:internal/process/task_queues:105:5)
	at async n._fetch (/home/emobilis/.vscode/extensions/github.copilot-chat-0.37.9/dist/extension.js:4862:26129)
	at async n.fetch (/home/emobilis/.vscode/extensions/github.copilot-chat-0.37.9/dist/extension.js:4862:25777)
	at async u (/home/emobilis/.vscode/extensions/github.copilot-chat-0.37.9/dist/extension.js:4894:190)
	at async CA.h (file:///usr/share/code/resources/app/out/vs/workbench/api/node/extensionHostProcess.js:116:41743)
  Error: getaddrinfo ENOTFOUND copilot-proxy.githubusercontent.com
  	at GetAddrInfoReqWrap.onlookupall [as oncomplete] (node:dns:122:26)

Connecting to https://mobile.events.data.microsoft.com: Error (2 ms): Error: net::ERR_NAME_NOT_RESOLVED
	at SimpleURLLoaderWrapper.<anonymous> (node:electron/js2c/utility_init:2:10684)
	at SimpleURLLoaderWrapper.emit (node:events:519:28)
  [object Object]
  {"is_request_error":true,"network_process_crashed":false}
Connecting to https://dc.services.visualstudio.com: Error (3 ms): Error: net::ERR_NAME_NOT_RESOLVED
	at SimpleURLLoaderWrapper.<anonymous> (node:electron/js2c/utility_init:2:10684)
	at SimpleURLLoaderWrapper.emit (node:events:519:28)
  [object Object]
  {"is_request_error":true,"network_process_crashed":false}
Connecting to https://copilot-telemetry.githubusercontent.com/_ping: Error (20 ms): Error: getaddrinfo ENOTFOUND copilot-telemetry.githubusercontent.com
	at GetAddrInfoReqWrap.onlookupall [as oncomplete] (node:dns:122:26)
Connecting to https://copilot-telemetry.githubusercontent.com/_ping: Error (20 ms): Error: getaddrinfo ENOTFOUND copilot-telemetry.githubusercontent.com
	at GetAddrInfoReqWrap.onlookupall [as oncomplete] (node:dns:122:26)
Connecting to https://default.exp-tas.com: Error (21 ms): Error: getaddrinfo ENOTFOUND default.exp-tas.com
	at GetAddrInfoReqWrap.onlookupall [as oncomplete] (node:dns:122:26)

Number of system certificates: 435

## Documentation

In corporate networks: [Troubleshooting firewall settings for GitHub Copilot](https://docs.github.com/en/copilot/troubleshooting-github-copilot/troubleshooting-firewall-settings-for-github-copilot).