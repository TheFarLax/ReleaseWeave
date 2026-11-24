# StudioNet deployments

Ten separate constructor transactions finalized successfully on StudioNet, chain ID 61999. The published source digest matches the corresponding local contract file.

| Contract | Contract explorer | Deployment receipt |
| --- | --- | --- |
| MigrationFence | [0xEB3f4bEB296169a7477358c5b2543e594507e029](https://explorer-studio.genlayer.com/address/0xEB3f4bEB296169a7477358c5b2543e594507e029) | [Transaction](https://explorer-studio.genlayer.com/tx/0xab3cd1e4c2296b84413ea57c5aef9eef76a0fa364bb16061942c07ddf2c0b4cb) |
| DependencyExit | [0x0a73707F01BC927ce4aCAe2C870e8149B67226a6](https://explorer-studio.genlayer.com/address/0x0a73707F01BC927ce4aCAe2C870e8149B67226a6) | [Transaction](https://explorer-studio.genlayer.com/tx/0x709c636448268cc8b9d70b0f62116a14dace0bf21fa687e973ebc340278e6154) |
| SplitLeakLedger | [0x90F78F15596A0DC328AA7DddB1d36136c2f22b5d](https://explorer-studio.genlayer.com/address/0x90F78F15596A0DC328AA7DddB1d36136c2f22b5d) | [Transaction](https://explorer-studio.genlayer.com/tx/0x300f5510e9962f21f580218406e44d74f675b797ec0c442b01bc9641c193d963) |
| LocaleParity | [0x2b34Ce43DeE666115736583bBAd47582e3cc9c88](https://explorer-studio.genlayer.com/address/0x2b34Ce43DeE666115736583bBAd47582e3cc9c88) | [Transaction](https://explorer-studio.genlayer.com/tx/0xf1d7fb440337c8f09513b5388a852a5b71179711ea5ee35cbe1dbaf9594f8272) |
| ReproQuorum | [0x6B306006bcD11a91822889C2335E8890B1dA024F](https://explorer-studio.genlayer.com/address/0x6B306006bcD11a91822889C2335E8890B1dA024F) | [Transaction](https://explorer-studio.genlayer.com/tx/0xd18ba8141bfdfc86ae603ec167db572669c2ee58c26677e4d002fc90a3f501da) |
| RegressionWitness | [0xE7e29c76B036d4451ec086c8F3A034Afea724725](https://explorer-studio.genlayer.com/address/0xE7e29c76B036d4451ec086c8F3A034Afea724725) | [Transaction](https://explorer-studio.genlayer.com/tx/0x0aebec44ef364d97ee12339bbc9612b1ce28f35f4998a3c0965ad63ba3ba1db7) |
| DeprecationPact | [0x958fbE365365c33d4dE0473Bf50811dD768C90f7](https://explorer-studio.genlayer.com/address/0x958fbE365365c33d4dE0473Bf50811dD768C90f7) | [Transaction](https://explorer-studio.genlayer.com/tx/0x70df5fca17fe693cecb53218f40e9076334ed18c5633b1e2b12e254bce49770a) |
| BuildOrigin | [0x8079C47C7fF52A25cA13D64521396B120Cc107E1](https://explorer-studio.genlayer.com/address/0x8079C47C7fF52A25cA13D64521396B120Cc107E1) | [Transaction](https://explorer-studio.genlayer.com/tx/0xb6e50b2248f00f36c1cdb0008d4227bf1dc50746f9218472a55e6803d9eab3e8) |
| BatchException | [0x6B540dc102405Ec1685DfFb097C4a165E110d6A5](https://explorer-studio.genlayer.com/address/0x6B540dc102405Ec1685DfFb097C4a165E110d6A5) | [Transaction](https://explorer-studio.genlayer.com/tx/0x225bb3a34bce150fce62f6b63ff51cc895a93de172d411058a4ed7082efe9ed6) |
| SchemaHandshake | [0xc2b7461735E26a092a6293ECDFDBA4C6080F3F4a](https://explorer-studio.genlayer.com/address/0xc2b7461735E26a092a6293ECDFDBA4C6080F3F4a) | [Transaction](https://explorer-studio.genlayer.com/tx/0x5522f9ae857ef78c968a32f400988c21018086835e6be55ff6d8794a894c601d) |

Every constructor takes zero arguments. The initial public count read returned 0 on each deployed instance. Run `npm run verify:live` to repeat the receipt and source checks.

The batch uses a dedicated StudioNet test wallet. Each user starts a workflow with their own `open(...)` call.
