Level 1:

# Marvel Chronicles !!!
----------



## TASK 1: Git Commands for Version Control

#### Basics:
- git branch 'name' creates it;
- git checkout 'name' switches the branch.
- git merge, combines both branches if they've have progressed, Git creates a new commit that ties the two histories together.
- git rebase , it creates a new commit to join two branches, rebase moves the entire feature branch so that it begins from the tip of the main branch.
> Git does not track "file changes" in the way traditional CVs (Concurrent Versions) do. Instead, it uses a Content-Addressable Filesystem.


![Image1](https://github.com/baswantrayallad/uvce-marvel-tasks/blob/main/TASK1%20git1.png?raw=true)
----------------------

![Image1](https://github.com/baswantrayallad/uvce-marvel-tasks/blob/main/TASK1%20git2.png?raw=true)
----------------------

![Image1](https://github.com/baswantrayallad/uvce-marvel-tasks/blob/main/TASK1%20git3.png?raw=true)
----------------------

![Image1](https://github.com/baswantrayallad/uvce-marvel-tasks/blob/main/TASK1%20git4.png?raw=true)
----------------------

----------

## TASK 3: Application on EC2 instance
I've used a virtual machine provisioned within  AWS Elastic Compute Cloud {EC2} ecosystem to host a Jenkins instance for CI & CD automation.
This Deployment utilizes a IAAS model 

#### Standard networking is often too slow for high-performance applications (like Big Data or ML).

**Enhanced Networking (ENA)**: Uses Single Root I/O Virtualization (SR-IOV) to provide higher I/O performance and lower CPU utilization. Essential for applications requiring high packet-per-second (PPS) performance.

**Elastic Fabric Adapter (EFA)**: A network interface for Amazon EC2 instances that enables you to run applications requiring high levels of inter-node communication (like High-Performance Computing) at scale.

![Image3](https://github.com/baswantrayallad/uvce-marvel-tasks/blob/main/Task3.png?raw=true)
![Image5](https://github.com/baswantrayallad/uvce-marvel-tasks/blob/main/Task3(1).png?raw=true)

![Image4](https://github.com/baswantrayallad/uvce-marvel-tasks/blob/main/Task3(2).png?raw=true)

---------------------------

## TASK 2 & TASK 4: AWS CloudFront & Dynomo DB 

DynamoDB is a fully managed NoSQL database service. Unlike traditional databases (like MySQL) that use tables with strict rows and columns, DynamoDB is designed for high-performance applications that need to scale massively

CloudFront is a Content Delivery Network (CDN). Its primary job is to speed up the distribution of your website’s content (like images, videos, or HTML files) to users across the globe.

![cloudfront](https://github.com/baswantrayallad/uvce-marvel-tasks/blob/main/Task2%26Task4(1).png?raw=true)

![Dynomo DB](https://github.com/baswantrayallad/uvce-marvel-tasks/blob/main/Task2%26Task4(2).png?raw=true)






## TASK 5: KALI Linux - 
**Infrastructure as Code**: The live-build Engine
Kali is not "installed" like Windows; it is "composed." The engineers use a framework called live-build.

**The Build Pipeline**: Instead of manually configuring a system, engineers define the OS in a Git repository (live-build-config). When they trigger a build, a script pulls the Debian core, overlays Kali-specific configurations, and "chroots" (changes root) into the environment to install 600+ tools.

**Metapackages**: To manage the massive toolset, Kali uses Metapackages (e.g., kali-linux-top10, kali-linux-headless). These are "empty" packages that contain a list of dependencies. Installing one metapackage triggers the logic to pull every tool required for that specific engineering role.

Social Engineering Attacks: 
![SET](https://github.com/baswantrayallad/uvce-marvel-tasks/blob/main/Task5.png?raw=true)

## TASK 6: Socket.IO

**Socket.IO** is more than just WebSockets. It is a management layer that sits on top of two sub-layers:

**Engine.IO**: The low-level engine that handles the connection. It first tries to connect via HTTP Long Polling for safety, then "upgrades" the connection to WebSockets for maximum speed.

**Packet Buffering**: If a user’s connection drops (e.g., they go through a tunnel), Socket.IO automatically buffers messages and sends them the moment they reconnect.

**Multiplexing** (Namespaces/Rooms): You can split one connection into multiple channels. For a chat app, "Rooms" allow you to isolate conversations so that User A and User B don't see User C's messages.

![Socket.io](https://github.com/baswantrayallad/uvce-marvel-tasks/blob/main/TASK6%20socket.io.png?raw=true)

## TASK 7: OSI

The OSI reference model
The OSI model is used to connect to the open systems—these are the systems that are open and communicate with other systems. By using this model, we do not depend on an operating system anymore, so we are allowed to communicate with any operating system on any computer. This model contains seven layers, where each layer has a specific function and defines the way data is handled on certain different layers. The seven layers that are contained in this model are the Physical layer, Data Link layer, Network layer, Transport layer, Session layer, Presentation layer, and the Application layer.

![osi](https://github.com/baswantrayallad/uvce-marvel-tasks/blob/main/Task7%20osi-model.png)

## TASK 8: IaaS, PaaS and SaaS

#### Infrastructure as a Service (IaaS)
Provides virtualized computing resources like servers, storage, and networking
Users have control over operating systems, applications, and storage.
Examples: Amazon Web Services (AWS) EC2, Google Compute Engine, Microsoft Azure.
Advantages:

**Scalability: Easily scale up/down based on demand.**
Cost-Effective: Pay only for what you use.
Full Control: You manage OS, storage, deployed apps, etc.
No Hardware Maintenance: Infrastructure is managed by the provider.
Disadvantages:

**Management Complexity: Requires skilled personnel to manage and configure.**
Security: You're responsible for securing your own apps and data.
Vendor Lock-in: Switching providers may be difficult.
Applications:

**Hosting websites or applications**
Storage, backup, and recovery
High-performance computing (HPC)
Development and testing environments
#### Platform as a Service (PaaS)
Delivers a platform that allows developers to build, test, and deploy applications without managing the underlying infrastructure.
Examples: Google App Engine, Microsoft Azure App Service, Heroku.
Advantages:

**Speed:** Quick development and deployment of apps.
No OS Maintenance: Provider manages OS, runtime, and middleware.
Built-in Tools: Database, DevOps, analytics, etc., are included.
Disadvantages:

**Limited Control:** Less control over underlying infrastructure.
Vendor Lock-in: Custom features may not be portable.
Runtime Restrictions: Limited to languages and frameworks supported by the provider.
Applications:

Application development frameworks
Business analytics and intelligence
API development and management

#### Software as a Service (SaaS)
Offers software applications over the internet on a subscription basis.
Examples: Microsoft 365, Salesforce, Google Workspace.
Advantages:

**No Installation Needed:** Access via browser or app.
Automatic Updates: Always up-to-date.
Accessibility: Accessible from anywhere with internet.
Disadvantages:

**Limited Customization:** Can't tweak core functionality.
Data Security: Sensitive data stored offsite.
Dependency: You're at the mercy of the provider’s uptime and policies.
Applications:

Email, collaboration tools, CRM
Document management
Accounting and billing systems

[![saas, paas, iaas](https://github.com/baswantrayallad/uvce-marvel-tasks/blob/main/Task8%20IPS.png)

[![saas, paas, iaas](https://github.com/baswantrayallad/uvce-marvel-tasks/blob/main/Task8%20IPS1.png)


## TASK 9: Encrypted  Messaging - Chat App
here am using PBKDF2 (Password-Based Key Derivation Function 2) it runs 100,000 iterations of hashing to turn a simple string into a cryptographically strong 256-bit key.
it uses a "salt" (kernel-chat-salt) which ensures that even if two rooms have the same password, their final encryption keys will be different.
The Encryption Algorithm (AES-256-GCM)
This is the "gold standard" of encryption.
AES-256, This is a symmetric-key algorithm used by governments and banks worldwide.

GCM (Galois/Counter Mode) is the "Mode" of operation. Unlike older modes, GCM provides Authenticated Encryption.

Integrity Check: GCM doesn't just hide the message; it also attaches a "tag." If someone tries to change even one bit of the encrypted data during transmission, the decryptMessage function will throw an error and refuse to show the message.
also the IV (Initialization Vector) -Point to this line in your code: crypto.getRandomValues(new Uint8Array(12)).
the IV is a unique "nonce" (number used once) for every single message.
so if we send the word "Hello" five times in a row, the Encrypted Data seen in the network tab will look completely different every time because the IV changes.

> This application uses End-to-End Encryption (E2EE). We derive a 256-bit key using PBKDF2 with 100k iterations. The actual encryption is AES-GCM, which ensures both Privacy (nobody can read it) and Integrity (nobody can alter it). As shown in the DevTools, the server only acts as a relay for raw ciphertext; it never possesses the keys to decrypt the traffic.


The Conclusion: This proves that without the exact derived key, the data is mathematically useless.
![enc](https://github.com/baswantrayallad/uvce-marvel-tasks/blob/main/Task9(1).png?raw=true)

![enc-dev](https://github.com/baswantrayallad/uvce-marvel-tasks/blob/main/Task9(2).png?raw=true)

## TASK 10: WEB SCRAPPING
Beautiful Soup is a Python library designed for parsing HTML and XML documents. It creates parse trees that make it straightforward to extract data from HTML documents you’ve scraped from the internet. Beautiful Soup is a useful tool in your web scraping toolkit, allowing you to conveniently extract specific information from HTML, even from complex static websites.

![webscraping](https://github.com/baswantrayallad/uvce-marvel-tasks/blob/main/Task10.png)
