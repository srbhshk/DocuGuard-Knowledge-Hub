{
  "success": true,
  "epics": [
    {
      "id": "978d9d0a-fc04-411d-aca0-0755eddf1d11",
      "title": "Usability, Accessibility, and Error Handling",
      "description": "This epic covers providing an accessible UI compliant with WCAG 2.1 AA, reducing friction in onboarding, and handling errors with clear user feedback.",
      "stories": [
        {
          "id": "1335140c-c61d-444f-bad1-76d05d49b0ed",
          "title": "Ensure First Query Setup Completes Within 10 Minutes",
          "description": "As an admin, I want to complete initial setup and run the first query within 10 minutes, so that onboarding is efficient",
          "epic": "epic-nfr-usability-accessibility-error-handling",
          "epicId": "978d9d0a-fc04-411d-aca0-0755eddf1d11",
          "priority": "high",
          "acceptanceCriteria": [
            "Functional: Setup wizard guides admin through workspace creation, document upload, and user assignment",
            "Functional: System provides progress indicators and tooltips",
            "Technical: Backend APIs respond quickly to setup requests",
            "Technical: Frontend UI optimized for quick navigation",
            "Technical: User feedback collected during pilot to validate timing"
          ],
          "estimatedEffort": 16,
          "storyPoints": 5,
          "dependencies": [
            "6208c1c5-76b6-4e31-a61a-774d544c7904",
            "f13817a7-d052-435f-9af4-d18438923327",
            "0b71d701-32b4-4653-815a-141f65c0ab36"
          ],
          "isSpike": false,
          "expectedOutcomes": [],
          "status": "approved",
          "llm_id": "us-043",
          "llmId": "us-043"
        },
        {
          "id": "0d7ea346-b931-4d35-b080-6581bb1c6caa",
          "title": "Provide Clear Error Messages and User Feedback",
          "description": "As a user, I want clear and actionable error messages, so that I can understand and resolve issues quickly",
          "epic": "epic-nfr-usability-accessibility-error-handling",
          "epicId": "978d9d0a-fc04-411d-aca0-0755eddf1d11",
          "priority": "high",
          "acceptanceCriteria": [
            "Functional: UI displays user-friendly error messages for common failures",
            "Functional: API returns standardized error codes and messages",
            "Technical: Frontend maps API errors to UI notifications",
            "Technical: Validation errors highlight specific input fields",
            "Technical: Error messages are logged for diagnostics"
          ],
          "estimatedEffort": 12,
          "storyPoints": 3,
          "dependencies": [
            "8492a709-2452-4f86-9abc-6e327ce60924",
            "62bd29d4-0f85-4ea8-b4f8-72745aab041d",
            "0b71d701-32b4-4653-815a-141f65c0ab36"
          ],
          "isSpike": false,
          "expectedOutcomes": [],
          "status": "approved",
          "llm_id": "us-042",
          "llmId": "us-042"
        },
        {
          "id": "45bc1336-5e4e-4faf-9370-389840a9dea6",
          "title": "Implement Accessible Frontend UI Components",
          "description": "As a knowledge worker, I want the UI to be accessible and compliant with WCAG 2.1 AA, so that I can use the system regardless of disabilities",
          "epic": "epic-nfr-usability-accessibility-error-handling",
          "epicId": "978d9d0a-fc04-411d-aca0-0755eddf1d11",
          "priority": "high",
          "acceptanceCriteria": [
            "Functional: UI components support keyboard navigation and screen readers",
            "Functional: Color contrast meets WCAG 2.1 AA standards",
            "Technical: Use Chakra UI accessibility features",
            "Technical: Accessibility tests performed with automated tools",
            "Technical: Accessibility issues fixed before release"
          ],
          "estimatedEffort": 16,
          "storyPoints": 5,
          "dependencies": [
            "6208c1c5-76b6-4e31-a61a-774d544c7904",
            "0b71d701-32b4-4653-815a-141f65c0ab36"
          ],
          "isSpike": false,
          "expectedOutcomes": [],
          "status": "approved",
          "llm_id": "us-041",
          "llmId": "us-041"
        }
      ],
      "spikeStories": []
    },
    {
      "id": "c1c888c6-926d-45a9-b821-b73b5523f921",
      "title": "Reliability, Uptime, and Disaster Recovery",
      "description": "This epic covers ensuring 99% uptime, graceful error handling, backup and restore procedures, and fault tolerance for the self-hosted system.",
      "stories": [
        {
          "id": "59b96aa7-bb5c-4018-9e9b-3dbc5c324c47",
          "title": "Provide Backup and Restore Procedures and Scripts",
          "description": "As a system administrator, I want documented backup and restore procedures and scripts, so that I can recover data in case of disaster",
          "epic": "epic-nfr-reliability-uptime-disaster-recovery",
          "epicId": "c1c888c6-926d-45a9-b821-b73b5523f921",
          "priority": "high",
          "acceptanceCriteria": [
            "Functional: Backup scripts export PostgreSQL data and file storage safely",
            "Functional: Restore scripts can recover system state from backups",
            "Technical: Qdrant snapshot and restore procedures documented",
            "Technical: Backup and restore tested end-to-end",
            "Technical: Documentation includes scheduling and verification steps"
          ],
          "estimatedEffort": 16,
          "storyPoints": 5,
          "dependencies": [
            "04a4eaea-8fa2-4d42-b43c-0dcd1c091cd1"
          ],
          "isSpike": false,
          "expectedOutcomes": [],
          "status": "approved",
          "llm_id": "us-040",
          "llmId": "us-040"
        },
        {
          "id": "0212c747-3a2f-4ab1-9669-3ff5606b978b",
          "title": "Implement Graceful Error Handling and Recovery",
          "description": "As the system, I want to handle errors gracefully and recover from failures without data loss, so that uptime and reliability are maximized",
          "epic": "epic-nfr-reliability-uptime-disaster-recovery",
          "epicId": "c1c888c6-926d-45a9-b821-b73b5523f921",
          "priority": "high",
          "acceptanceCriteria": [
            "Functional: API returns standardized error responses with meaningful messages",
            "Functional: System retries transient failures where appropriate",
            "Technical: Unhandled exceptions are logged and do not crash services",
            "Technical: Services restart automatically on failure in Docker Compose",
            "Technical: Health endpoints report service status accurately"
          ],
          "estimatedEffort": 12,
          "storyPoints": 5,
          "dependencies": [
            "8492a709-2452-4f86-9abc-6e327ce60924",
            "62bd29d4-0f85-4ea8-b4f8-72745aab041d",
            "9d9a1745-8f55-42e4-b237-0f5efd391741",
            "04a4eaea-8fa2-4d42-b43c-0dcd1c091cd1"
          ],
          "isSpike": false,
          "expectedOutcomes": [],
          "status": "approved",
          "llm_id": "us-039",
          "llmId": "us-039"
        }
      ],
      "spikeStories": []
    },
    {
      "id": "fc9782b9-5ac2-4b91-b4fa-9c35c874401a",
      "title": "Monitoring, Logging, and Observability",
      "description": "This epic covers implementing logging, metrics collection, alerting, and observability to ensure system health and quick issue detection.",
      "stories": [
        {
          "id": "54f04eec-eb67-44c6-9b63-9296b9246396",
          "title": "Set Up Metrics Collection and Alerting",
          "description": "As the system, I want to collect metrics like query latency, upload success, and error rates, and configure alerts, so that system health is monitored proactively",
          "epic": "epic-nfr-monitoring-logging-alerts",
          "epicId": "fc9782b9-5ac2-4b91-b4fa-9c35c874401a",
          "priority": "medium",
          "acceptanceCriteria": [
            "Functional: Metrics are collected and exposed via Prometheus endpoints",
            "Functional: Alerts are configured for failed uploads, permission errors, and high latency",
            "Technical: Grafana dashboards created for key metrics",
            "Technical: Alert notifications sent to configured channels",
            "Technical: Monitoring components deployed in Docker Compose"
          ],
          "estimatedEffort": 16,
          "storyPoints": 5,
          "dependencies": [
            "04a4eaea-8fa2-4d42-b43c-0dcd1c091cd1"
          ],
          "isSpike": false,
          "expectedOutcomes": [],
          "status": "approved",
          "llm_id": "us-038",
          "llmId": "us-038"
        },
        {
          "id": "357fdd09-4a93-4edc-89fb-feb7aba83f9a",
          "title": "Implement Structured Logging for Backend Services",
          "description": "As the system, I want to implement structured logging with appropriate levels and context, so that issues can be diagnosed efficiently",
          "epic": "epic-nfr-monitoring-logging-alerts",
          "epicId": "fc9782b9-5ac2-4b91-b4fa-9c35c874401a",
          "priority": "high",
          "acceptanceCriteria": [
            "Functional: All API calls, ingestion, and query events are logged with structured JSON format",
            "Technical: Logs include timestamps, user IDs, request IDs, and error details",
            "Technical: Sensitive data is excluded from logs",
            "Technical: Logs are written to stdout and file with rotation",
            "Technical: Logging configuration supports level adjustment"
          ],
          "estimatedEffort": 12,
          "storyPoints": 5,
          "dependencies": [
            "8492a709-2452-4f86-9abc-6e327ce60924",
            "62bd29d4-0f85-4ea8-b4f8-72745aab041d",
            "9d9a1745-8f55-42e4-b237-0f5efd391741"
          ],
          "isSpike": false,
          "expectedOutcomes": [],
          "status": "approved",
          "llm_id": "us-037",
          "llmId": "us-037"
        }
      ],
      "spikeStories": []
    },
    {
      "id": "4f341213-9613-4bae-887e-da48eca79d46",
      "title": "Open-Source Component Usage",
      "description": "This epic ensures the use of open-source backend and frontend frameworks and avoids proprietary or opinionated libraries to maintain transparency and avoid vendor lock-in.",
      "stories": [
        {
          "id": "9bf767df-c5e6-44f9-8d1f-257f72c4f7fc",
          "title": "Use Open-Source Backend and Frontend Frameworks",
          "description": "As the system architect, I want to use open-source frameworks like FastAPI, React, Qdrant, and Ollama, so that the system remains transparent and vendor-neutral",
          "epic": "epic-nfr-open-source-component-usage",
          "epicId": "4f341213-9613-4bae-887e-da48eca79d46",
          "priority": "high",
          "acceptanceCriteria": [
            "Functional: All core components use open-source licenses",
            "Technical: No proprietary or opinionated libraries like LangChain are used",
            "Technical: Custom RAG pipeline implemented without third-party abstraction layers",
            "Technical: Dependencies are documented and regularly audited",
            "Technical: Community-supported versions of components are used"
          ],
          "estimatedEffort": 8,
          "storyPoints": 3,
          "dependencies": [],
          "isSpike": false,
          "expectedOutcomes": [],
          "status": "approved",
          "llm_id": "us-036",
          "llmId": "us-036"
        }
      ],
      "spikeStories": []
    },
    {
      "id": "7abab78f-dd94-44bd-9569-eee8992e8d8b",
      "title": "Performance and Latency Targets",
      "description": "This epic covers maintaining query response latency under 3 seconds by optimizing the RAG pipeline, vector search, and local LLM inference.",
      "stories": [
        {
          "id": "f3a09f78-2f24-4cd6-8f65-a205c23058d5",
          "title": "Implement Backend Performance Tuning and Monitoring",
          "description": "As the system, I want to tune backend performance and monitor key metrics to maintain smooth user experience",
          "epic": "epic-nfr-performance-latency",
          "epicId": "7abab78f-dd94-44bd-9569-eee8992e8d8b",
          "priority": "high",
          "acceptanceCriteria": [
            "Functional: Backend APIs respond within target times under load",
            "Technical: Database connection pooling configured",
            "Technical: API rate limiting implemented",
            "Technical: Metrics collected for response times and error rates",
            "Technical: Alerts configured for performance degradation"
          ],
          "estimatedEffort": 16,
          "storyPoints": 5,
          "dependencies": [
            "8492a709-2452-4f86-9abc-6e327ce60924",
            "62bd29d4-0f85-4ea8-b4f8-72745aab041d",
            "9d9a1745-8f55-42e4-b237-0f5efd391741"
          ],
          "isSpike": false,
          "expectedOutcomes": [],
          "status": "approved",
          "llm_id": "us-035",
          "llmId": "us-035"
        },
        {
          "id": "de91b0cd-2593-4b5d-bf67-9b93ad16cb34",
          "title": "Optimize RAG Pipeline for Low Latency",
          "description": "As the system, I want to optimize the RAG pipeline components to ensure query response latency is under 3 seconds at 95th percentile",
          "epic": "epic-nfr-performance-latency",
          "epicId": "7abab78f-dd94-44bd-9569-eee8992e8d8b",
          "priority": "high",
          "acceptanceCriteria": [
            "Functional: Query response times measured and meet latency targets",
            "Technical: Pipeline components are profiled and bottlenecks identified",
            "Technical: Parallelization or caching applied where beneficial",
            "Technical: Load testing simulates expected query volumes",
            "Technical: Monitoring metrics collected for latency"
          ],
          "estimatedEffort": 20,
          "storyPoints": 8,
          "dependencies": [
            "f882cf33-6f83-48a9-b580-5fe62d87fa09",
            "203cf20a-c961-4ad7-a28b-813eca8fd4b5",
            "b2731712-f394-470f-a017-f4d0d2f1b27b"
          ],
          "isSpike": false,
          "expectedOutcomes": [],
          "status": "approved",
          "llm_id": "us-034",
          "llmId": "us-034"
        }
      ],
      "spikeStories": []
    },
    {
      "id": "8c011662-b385-416b-9fd3-7cdf12293fc4",
      "title": "Data Security and Access Control",
      "description": "This epic covers ensuring robust security to protect sensitive enterprise data with enforced permissions, secure authentication, and compliance with regulations.",
      "stories": [
        {
          "id": "ec45289b-a5b2-4cee-856a-fcdca5b2d616",
          "title": "Plan Document-Level Permissions for Future Release",
          "description": "As the system architect, I want to design document-level permissions for v2, so that finer-grained access control can be implemented later",
          "epic": "epic-nfr-data-security-access-control",
          "epicId": "8c011662-b385-416b-9fd3-7cdf12293fc4",
          "priority": "medium",
          "acceptanceCriteria": [
            "Design document-level permission model documented",
            "Data schema extensions proposed for document-level ACLs",
            "API design for document-level permission management drafted",
            "Security implications and compliance considerations analyzed",
            "Implementation plan and roadmap created"
          ],
          "estimatedEffort": 16,
          "storyPoints": 5,
          "dependencies": [],
          "isSpike": false,
          "expectedOutcomes": [],
          "status": "approved",
          "llm_id": "us-033",
          "llmId": "us-033"
        },
        {
          "id": "83204155-76db-4820-8d5d-f90272d0f39c",
          "title": "Integrate Enterprise SSO for Secure Authentication",
          "description": "As an enterprise user, I want to authenticate securely via SAML/OIDC SSO, so that access complies with corporate security policies",
          "epic": "epic-nfr-data-security-access-control",
          "epicId": "8c011662-b385-416b-9fd3-7cdf12293fc4",
          "priority": "high",
          "acceptanceCriteria": [
            "Functional: SSO login supports major IdPs like Okta, Azure AD, Google Workspace",
            "Functional: Authentication tokens are securely handled and validated",
            "Technical: Use secure session management and JWT signing",
            "Technical: SSO configurations are encrypted and stored securely",
            "Technical: Audit logs record all authentication events"
          ],
          "estimatedEffort": 24,
          "storyPoints": 8,
          "dependencies": [
            "4bc93892-023b-460f-adc3-a7179c81b722",
            "9cb4b78a-4931-4001-a971-c41d0bd03860",
            "16d112e4-ae39-4d67-bf88-5fc6be123d36"
          ],
          "isSpike": false,
          "expectedOutcomes": [],
          "status": "approved",
          "llm_id": "us-032",
          "llmId": "us-032"
        },
        {
          "id": "41b28af8-b288-4441-a849-975a2794a104",
          "title": "Enforce Collection-Level Permissions in API and Query Layer",
          "description": "As the system, I want to enforce collection-level permissions on all API and query operations, so that users only access authorized documents",
          "epic": "epic-nfr-data-security-access-control",
          "epicId": "8c011662-b385-416b-9fd3-7cdf12293fc4",
          "priority": "high",
          "acceptanceCriteria": [
            "Functional: API returns 403 Forbidden for unauthorized collection access",
            "Functional: Query results only include documents from permitted collections",
            "Technical: Permissions checks integrated in API middleware and query handlers",
            "Technical: Unit and integration tests cover permission enforcement",
            "Technical: Audit logs record permission violations"
          ],
          "estimatedEffort": 20,
          "storyPoints": 8,
          "dependencies": [
            "a23bb700-bd6a-4d83-8229-e926c0733b23"
          ],
          "isSpike": false,
          "expectedOutcomes": [],
          "status": "approved",
          "llm_id": "us-031",
          "llmId": "us-031"
        }
      ],
      "spikeStories": []
    },
    {
      "id": "48a8a9b1-8722-4db3-b976-dd401b90964a",
      "title": "Scalability for Growing Organizations",
      "description": "This epic covers designing infrastructure to handle growth from initial small deployments to larger organizations with increased users, documents, and query volumes while maintaining performance.",
      "stories": [
        {
          "id": "ca7a6981-1f47-4709-9992-2cfcaacb9fff",
          "title": "Implement Database Indexing and Query Optimization",
          "description": "As the system, I want to optimize PostgreSQL database indexes and queries to support large user and document volumes efficiently",
          "epic": "epic-infrastructure-scalability",
          "epicId": "48a8a9b1-8722-4db3-b976-dd401b90964a",
          "priority": "medium",
          "acceptanceCriteria": [
            "Functional: Database queries for user, document, and collection data are performant",
            "Technical: Indexes created on frequently queried columns",
            "Technical: Query plans analyzed and optimized",
            "Technical: Database connection pooling configured",
            "Technical: Performance tests validate query response times"
          ],
          "estimatedEffort": 16,
          "storyPoints": 5,
          "dependencies": [
            "45f008df-44fb-4233-b644-e9858cd3b759",
            "42dd9560-1229-4fd2-b77c-0448d25409dd"
          ],
          "isSpike": false,
          "expectedOutcomes": [],
          "status": "approved",
          "llm_id": "us-030",
          "llmId": "us-030"
        },
        {
          "id": "b2731712-f394-470f-a017-f4d0d2f1b27b",
          "title": "Optimize Local LLM Inference Performance",
          "description": "As the system, I want to optimize Ollama LLM inference performance to support up to 500 queries per day per organization with low latency",
          "epic": "epic-infrastructure-scalability",
          "epicId": "48a8a9b1-8722-4db3-b976-dd401b90964a",
          "priority": "medium",
          "acceptanceCriteria": [
            "Functional: LLM inference latency measured and optimized",
            "Technical: Model quantization or size configuration supported",
            "Technical: Resource usage monitored and optimized",
            "Technical: Failover or retry logic implemented for LLM errors",
            "Technical: Performance tests validate throughput targets"
          ],
          "estimatedEffort": 16,
          "storyPoints": 5,
          "dependencies": [
            "b4a74558-170a-4610-8b22-0c51fefee1fa"
          ],
          "isSpike": false,
          "expectedOutcomes": [],
          "status": "approved",
          "llm_id": "us-029",
          "llmId": "us-029"
        },
        {
          "id": "203cf20a-c961-4ad7-a28b-813eca8fd4b5",
          "title": "Optimize Vector Search Performance with Qdrant",
          "description": "As the system, I want to optimize Qdrant vector search performance to handle up to 50,000 documents per organization, so that query latency remains under 3 seconds",
          "epic": "epic-infrastructure-scalability",
          "epicId": "48a8a9b1-8722-4db3-b976-dd401b90964a",
          "priority": "medium",
          "acceptanceCriteria": [
            "Functional: Vector search latency measured and optimized under load",
            "Technical: Qdrant indexing parameters tuned for large datasets",
            "Technical: Query caching or batching strategies evaluated",
            "Technical: Performance tests simulate target query volumes",
            "Technical: Monitoring metrics collected for query latency"
          ],
          "estimatedEffort": 20,
          "storyPoints": 8,
          "dependencies": [
            "fbf00704-6f6c-466e-bf5a-1119edb5c9ba"
          ],
          "isSpike": false,
          "expectedOutcomes": [],
          "status": "approved",
          "llm_id": "us-028",
          "llmId": "us-028"
        }
      ],
      "spikeStories": []
    },
    {
      "id": "d01b1200-7fb4-461a-a21d-aeff2664f63c",
      "title": "Self-Hosted Deployment via Docker Compose",
      "description": "This epic covers the deployment model where customers download and run the system on their own infrastructure using Docker Compose, including containerization and documentation.",
      "stories": [
        {
          "id": "d47e24b1-bc42-4a25-a9c0-5056a6850178",
          "title": "Document Installation and Operation Guide for Self-Hosted Deployment",
          "description": "As a customer, I want clear documentation on how to install, configure, and operate the system using Docker Compose, so that I can deploy and maintain it successfully",
          "epic": "epic-infrastructure-self-hosted-deployment",
          "epicId": "d01b1200-7fb4-461a-a21d-aeff2664f63c",
          "priority": "high",
          "acceptanceCriteria": [
            "Functional: Documentation covers prerequisites, installation steps, and configuration",
            "Functional: Troubleshooting and common issues are described",
            "Technical: Instructions include environment variable setup and secret management",
            "Technical: Guide includes backup and restore procedures",
            "Technical: Documentation is accessible in the repository and website"
          ],
          "estimatedEffort": 12,
          "storyPoints": 3,
          "dependencies": [
            "04a4eaea-8fa2-4d42-b43c-0dcd1c091cd1"
          ],
          "isSpike": false,
          "expectedOutcomes": [],
          "status": "approved",
          "llm_id": "us-027",
          "llmId": "us-027"
        },
        {
          "id": "04a4eaea-8fa2-4d42-b43c-0dcd1c091cd1",
          "title": "Create Docker Compose Configuration for All Components",
          "description": "As the system, I want to provide a Docker Compose configuration that orchestrates backend, frontend, Qdrant, Ollama, and PostgreSQL, so that customers can deploy the system easily",
          "epic": "epic-infrastructure-self-hosted-deployment",
          "epicId": "d01b1200-7fb4-461a-a21d-aeff2664f63c",
          "priority": "high",
          "acceptanceCriteria": [
            "Functional: Docker Compose file defines all required services with correct networking",
            "Functional: Services start and communicate correctly on a single host",
            "Technical: Persistent volumes configured for data storage",
            "Technical: Environment variables and secrets managed securely",
            "Technical: Compose file supports configuration overrides"
          ],
          "estimatedEffort": 16,
          "storyPoints": 5,
          "dependencies": [],
          "isSpike": false,
          "expectedOutcomes": [],
          "status": "approved",
          "llm_id": "us-026",
          "llmId": "us-026"
        }
      ],
      "spikeStories": []
    },
    {
      "id": "f1e1cc77-d778-46af-8e1e-ec8676f2f989",
      "title": "File Upload Support",
      "description": "This epic covers support for uploading files in PDF, DOCX, and TXT formats at launch, with plans for connectors to external document sources post-launch.",
      "stories": [
        {
          "id": "92806d55-ac0d-4cda-94e9-f9f33c5fd0b2",
          "title": "Design API Connectors for External Document Sources (Post-Launch Spike)",
          "description": "As a developer, I want to research and design API connectors for Confluence, Notion, Google Drive, and SharePoint, so that future versions can import documents from these sources",
          "epic": "epic-integration-file-upload-support",
          "epicId": "f1e1cc77-d778-46af-8e1e-ec8676f2f989",
          "priority": "medium",
          "acceptanceCriteria": [
            "Research completed for each external API's authentication and data retrieval",
            "Design documented for connector architecture and integration points",
            "Proof-of-concept code snippets or SDK usage examples provided",
            "Integration challenges and limitations identified",
            "Recommendations for phased implementation prioritized"
          ],
          "estimatedEffort": 24,
          "storyPoints": 8,
          "dependencies": [],
          "isSpike": false,
          "expectedOutcomes": [],
          "status": "approved",
          "llm_id": "us-025",
          "llmId": "us-025"
        },
        {
          "id": "dc5cef48-815b-4348-baea-08b9b539f45e",
          "title": "Support File Uploads for PDF, DOCX, and TXT Formats",
          "description": "As an editor, I want to upload PDF, DOCX, and TXT files, so that I can add diverse document types to the knowledge base",
          "epic": "epic-integration-file-upload-support",
          "epicId": "f1e1cc77-d778-46af-8e1e-ec8676f2f989",
          "priority": "high",
          "acceptanceCriteria": [
            "Functional: System accepts PDF, DOCX, and TXT files via upload API",
            "Functional: Files are validated for type and size before acceptance",
            "Technical: Backend uses file parsing libraries for all three formats",
            "Technical: Uploaded files are stored and indexed correctly",
            "Technical: Frontend upload UI supports all three file types"
          ],
          "estimatedEffort": 16,
          "storyPoints": 5,
          "dependencies": [
            "e4568bdb-c319-4ed5-8899-4c1d85757305",
            "87772124-3bce-4461-be87-8a0c4b2ed6a8"
          ],
          "isSpike": false,
          "expectedOutcomes": [],
          "status": "approved",
          "llm_id": "us-024",
          "llmId": "us-024"
        }
      ],
      "spikeStories": []
    },
    {
      "id": "bf4bfece-d2fd-4d9a-8fc9-a7d83f781c2b",
      "title": "SSO Integration (SAML/OIDC)",
      "description": "This epic covers the implementation of single sign-on integration using SAML and OIDC protocols, enabling secure enterprise authentication and seamless user access.",
      "stories": [
        {
          "id": "4e9cef6c-7a55-4e5a-8097-2cd159a4027b",
          "title": "Integrate SSO Authentication with User and Permission Management",
          "description": "As the system, I want to link SSO authenticated users with internal user roles and collection assignments, so that permissions are enforced correctly",
          "epic": "epic-integration-sso",
          "epicId": "bf4bfece-d2fd-4d9a-8fc9-a7d83f781c2b",
          "priority": "high",
          "acceptanceCriteria": [
            "Functional: SSO login creates or links user accounts in PostgreSQL",
            "Functional: User roles and collection assignments are loaded post-login",
            "Technical: JWT tokens include user roles and collection claims",
            "Technical: Permissions engine uses SSO user identity for access control",
            "Technical: Audit logs record SSO login events"
          ],
          "estimatedEffort": 16,
          "storyPoints": 5,
          "dependencies": [
            "9cb4b78a-4931-4001-a971-c41d0bd03860",
            "16d112e4-ae39-4d67-bf88-5fc6be123d36",
            "42dd9560-1229-4fd2-b77c-0448d25409dd",
            "a23bb700-bd6a-4d83-8229-e926c0733b23"
          ],
          "isSpike": false,
          "expectedOutcomes": [],
          "status": "approved",
          "llm_id": "us-023",
          "llmId": "us-023"
        },
        {
          "id": "16d112e4-ae39-4d67-bf88-5fc6be123d36",
          "title": "Implement OIDC Authentication Flow",
          "description": "As an enterprise user, I want to authenticate via OIDC SSO, so that I can securely access the system using my corporate credentials",
          "epic": "epic-integration-sso",
          "epicId": "bf4bfece-d2fd-4d9a-8fc9-a7d83f781c2b",
          "priority": "high",
          "acceptanceCriteria": [
            "Functional: System supports OIDC authorization code flow with major IdPs",
            "Functional: System exchanges code for tokens and validates ID token",
            "Technical: Use Authlib library for OIDC protocol handling",
            "Technical: OIDC client configuration is per organization",
            "Technical: Tokens stored securely and used for session management"
          ],
          "estimatedEffort": 24,
          "storyPoints": 8,
          "dependencies": [],
          "isSpike": false,
          "expectedOutcomes": [],
          "status": "approved",
          "llm_id": "us-022",
          "llmId": "us-022"
        },
        {
          "id": "9cb4b78a-4931-4001-a971-c41d0bd03860",
          "title": "Implement SAML Authentication Flow",
          "description": "As an enterprise user, I want to authenticate via SAML SSO, so that I can securely access the system using my corporate credentials",
          "epic": "epic-integration-sso",
          "epicId": "bf4bfece-d2fd-4d9a-8fc9-a7d83f781c2b",
          "priority": "high",
          "acceptanceCriteria": [
            "Functional: System initiates SAML authentication with configured IdP",
            "Functional: System processes SAML assertions and creates user sessions",
            "Technical: Use python-saml library for SAML protocol handling",
            "Technical: SAML metadata configurable per organization",
            "Technical: Errors in SAML flow handled gracefully with user feedback"
          ],
          "estimatedEffort": 24,
          "storyPoints": 8,
          "dependencies": [],
          "isSpike": false,
          "expectedOutcomes": [],
          "status": "approved",
          "llm_id": "us-021",
          "llmId": "us-021"
        }
      ],
      "spikeStories": []
    },
    {
      "id": "30f2d4cf-1d59-4659-9dba-41436f4e6470",
      "title": "User Workflow and Onboarding",
      "description": "This epic covers the smooth first-use experience where an admin creates a workspace, uploads documents, assigns users, and users query documents, reducing friction for teams to start using the system quickly.",
      "stories": [
        {
          "id": "0b71d701-32b4-4653-815a-141f65c0ab36",
          "title": "Implement Simple Login and Query Interface for Users",
          "description": "As a viewer or editor, I want to log in and query documents easily, so that I can find information quickly",
          "epic": "epic-core-user-workflow-onboarding",
          "epicId": "30f2d4cf-1d59-4659-9dba-41436f4e6470",
          "priority": "high",
          "acceptanceCriteria": [
            "Functional: Users can log in via SSO or local fallback",
            "Functional: Users see a simple search bar to enter queries",
            "Functional: Query results display answers with citations and links",
            "Technical: Frontend React components for login and search",
            "Technical: Backend supports authentication and query APIs"
          ],
          "estimatedEffort": 20,
          "storyPoints": 8,
          "dependencies": [
            "4bc93892-023b-460f-adc3-a7179c81b722",
            "f882cf33-6f83-48a9-b580-5fe62d87fa09"
          ],
          "isSpike": false,
          "expectedOutcomes": [],
          "status": "approved",
          "llm_id": "us-020",
          "llmId": "us-020"
        },
        {
          "id": "f13817a7-d052-435f-9af4-d18438923327",
          "title": "Implement User Creation and Assignment by Admin",
          "description": "As an admin, I want to create users and assign them to collections, so that team members can access relevant documents",
          "epic": "epic-core-user-workflow-onboarding",
          "epicId": "30f2d4cf-1d59-4659-9dba-41436f4e6470",
          "priority": "high",
          "acceptanceCriteria": [
            "Functional: Admin can create users and assign roles and collections",
            "Functional: Users receive invitation or notification to log in",
            "Technical: Backend APIs support user creation and assignment",
            "Technical: Frontend UI supports user management and assignment",
            "Technical: Permissions enforced on user assignments"
          ],
          "estimatedEffort": 20,
          "storyPoints": 8,
          "dependencies": [
            "42dd9560-1229-4fd2-b77c-0448d25409dd",
            "45f008df-44fb-4233-b644-e9858cd3b759",
            "e7aa8ab6-008f-4b8c-8ad4-570257d5ca06"
          ],
          "isSpike": false,
          "expectedOutcomes": [],
          "status": "approved",
          "llm_id": "us-019",
          "llmId": "us-019"
        },
        {
          "id": "6208c1c5-76b6-4e31-a61a-774d544c7904",
          "title": "Implement Admin Sign-Up and Workspace Creation Flow",
          "description": "As an admin, I want to sign up and create a workspace, so that I can start using the system",
          "epic": "epic-core-user-workflow-onboarding",
          "epicId": "30f2d4cf-1d59-4659-9dba-41436f4e6470",
          "priority": "high",
          "acceptanceCriteria": [
            "Functional: Admin can register and create workspace via frontend UI",
            "Functional: Workspace is created with default settings and initial collection",
            "Technical: Backend supports workspace creation APIs",
            "Technical: Frontend provides guided setup wizard",
            "Technical: User session established post sign-up"
          ],
          "estimatedEffort": 16,
          "storyPoints": 5,
          "dependencies": [
            "4bc93892-023b-460f-adc3-a7179c81b722",
            "45f008df-44fb-4233-b644-e9858cd3b759"
          ],
          "isSpike": false,
          "expectedOutcomes": [],
          "status": "approved",
          "llm_id": "us-018",
          "llmId": "us-018"
        }
      ],
      "spikeStories": []
    },
    {
      "id": "3b7c566d-692f-4742-8a3a-06c35f512844",
      "title": "API-First Design",
      "description": "This epic covers exposing all core functionalities via REST APIs, including document upload, querying, user and permission management, with API documentation and versioning.",
      "stories": [
        {
          "id": "9d9a1745-8f55-42e4-b237-0f5efd391741",
          "title": "Design and Implement REST API Endpoint for Natural Language Querying",
          "description": "As a viewer, I want to query documents via REST API, so that I can integrate search into other applications",
          "epic": "epic-core-api-first-design",
          "epicId": "3b7c566d-692f-4742-8a3a-06c35f512844",
          "priority": "high",
          "acceptanceCriteria": [
            "Functional: API accepts question and collection_id, returns answer with citations",
            "Functional: API enforces rate limiting and permissions",
            "Technical: API integrates with RAG pipeline components",
            "Technical: API returns consistent JSON schema for answers and citations",
            "Technical: API documented and versioned"
          ],
          "estimatedEffort": 16,
          "storyPoints": 5,
          "dependencies": [
            "f882cf33-6f83-48a9-b580-5fe62d87fa09",
            "a23bb700-bd6a-4d83-8229-e926c0733b23"
          ],
          "isSpike": false,
          "expectedOutcomes": [],
          "status": "approved",
          "llm_id": "us-017",
          "llmId": "us-017"
        },
        {
          "id": "62bd29d4-0f85-4ea8-b4f8-72745aab041d",
          "title": "Design and Implement REST API Endpoints for Document and Collection Management",
          "description": "As an editor or admin, I want to manage documents and collections via REST APIs, so that I can integrate with other tools",
          "epic": "epic-core-api-first-design",
          "epicId": "3b7c566d-692f-4742-8a3a-06c35f512844",
          "priority": "high",
          "acceptanceCriteria": [
            "Functional: API supports CRUD operations for collections and documents",
            "Functional: API supports file upload via multipart/form-data",
            "Technical: API endpoints enforce permissions and validate inputs",
            "Technical: API supports pagination and filtering where applicable",
            "Technical: API documented with OpenAPI and versioned"
          ],
          "estimatedEffort": 24,
          "storyPoints": 8,
          "dependencies": [
            "45f008df-44fb-4233-b644-e9858cd3b759",
            "e53e9568-7744-4ea0-b8bd-21f00bf99b30",
            "a23bb700-bd6a-4d83-8229-e926c0733b23"
          ],
          "isSpike": false,
          "expectedOutcomes": [],
          "status": "approved",
          "llm_id": "us-016",
          "llmId": "us-016"
        },
        {
          "id": "8492a709-2452-4f86-9abc-6e327ce60924",
          "title": "Design and Implement REST API Endpoints for User Management",
          "description": "As an admin, I want to manage users via REST APIs, so that I can automate user administration",
          "epic": "epic-core-api-first-design",
          "epicId": "3b7c566d-692f-4742-8a3a-06c35f512844",
          "priority": "high",
          "acceptanceCriteria": [
            "Functional: API supports listing, creating, updating, and deleting users",
            "Functional: API enforces role-based access control",
            "Technical: Endpoints documented with OpenAPI schema",
            "Technical: API versioning implemented under /api/v1/",
            "Technical: API returns standardized error codes and messages"
          ],
          "estimatedEffort": 20,
          "storyPoints": 8,
          "dependencies": [
            "42dd9560-1229-4fd2-b77c-0448d25409dd",
            "4bc93892-023b-460f-adc3-a7179c81b722"
          ],
          "isSpike": false,
          "expectedOutcomes": [],
          "status": "approved",
          "llm_id": "us-015",
          "llmId": "us-015"
        }
      ],
      "spikeStories": []
    },
    {
      "id": "57a468cd-bb72-47cc-bb26-380e722c94ce",
      "title": "Multi-Tenant Architecture (Deferred)",
      "description": "This epic covers the design and implementation of multi-tenant support with isolated data and permissions per organization, planned for post-v1 releases.",
      "stories": [
        {
          "id": "a89cc6b2-a780-4e27-8ab0-1e1cc1ac38e5",
          "title": "Implement Tenant-Aware API Endpoints",
          "description": "As the system, I want API endpoints to be tenant-aware, so that data returned and modified is scoped to the authenticated user's organization",
          "epic": "epic-core-multi-tenant-architecture",
          "epicId": "57a468cd-bb72-47cc-bb26-380e722c94ce",
          "priority": "medium",
          "acceptanceCriteria": [
            "Functional: API endpoints filter data by organization context",
            "Functional: Users cannot access data from other organizations",
            "Technical: TenantResolver middleware extracts organization from JWT claims",
            "Technical: Database queries include organization_id filters",
            "Technical: API returns 403 on cross-tenant access attempts"
          ],
          "estimatedEffort": 20,
          "storyPoints": 8,
          "dependencies": [
            "724755ec-81b0-4475-9b9d-3decf0309f03",
            "4bc93892-023b-460f-adc3-a7179c81b722"
          ],
          "isSpike": false,
          "expectedOutcomes": [],
          "status": "approved",
          "llm_id": "us-014",
          "llmId": "us-014"
        },
        {
          "id": "724755ec-81b0-4475-9b9d-3decf0309f03",
          "title": "Design Multi-Tenant Data Model in PostgreSQL",
          "description": "As the system architect, I want to design a multi-tenant data model that isolates organizations' data, so that multiple companies can securely use the platform",
          "epic": "epic-core-multi-tenant-architecture",
          "epicId": "57a468cd-bb72-47cc-bb26-380e722c94ce",
          "priority": "medium",
          "acceptanceCriteria": [
            "Functional: Data model supports organization isolation for users, collections, documents",
            "Technical: PostgreSQL schema includes organizations and organization_id foreign keys",
            "Technical: Data access queries are tenant-aware and filter by organization",
            "Technical: Migration scripts created to add multi-tenant support",
            "Technical: Model supports future tenant-aware API endpoints"
          ],
          "estimatedEffort": 16,
          "storyPoints": 5,
          "dependencies": [
            "42dd9560-1229-4fd2-b77c-0448d25409dd"
          ],
          "isSpike": false,
          "expectedOutcomes": [],
          "status": "approved",
          "llm_id": "us-013",
          "llmId": "us-013"
        }
      ],
      "spikeStories": []
    },
    {
      "id": "f8082d2b-842e-4d99-8694-bff52e87c167",
      "title": "Basic Permissions Layer",
      "description": "This epic covers the implementation of a simple permissions system with three roles and collection-level access control, integrated with SSO authentication.",
      "stories": [
        {
          "id": "4bc93892-023b-460f-adc3-a7179c81b722",
          "title": "Integrate SSO Authentication with Permissions",
          "description": "As the system, I want to integrate SAML/OIDC SSO authentication with user and permission management, so that enterprise users can securely log in",
          "epic": "epic-core-permissions-layer",
          "epicId": "f8082d2b-842e-4d99-8694-bff52e87c167",
          "priority": "high",
          "acceptanceCriteria": [
            "Functional: Users can authenticate via SAML and OIDC SSO providers",
            "Functional: SSO login creates or links user accounts with roles and collections",
            "Technical: Authentication middleware supports SAML and OIDC protocols",
            "Technical: JWT tokens issued post-authentication with user claims",
            "Technical: Session management and token validation implemented"
          ],
          "estimatedEffort": 24,
          "storyPoints": 8,
          "dependencies": [],
          "isSpike": false,
          "expectedOutcomes": [],
          "status": "approved",
          "llm_id": "us-012",
          "llmId": "us-012"
        },
        {
          "id": "a23bb700-bd6a-4d83-8229-e926c0733b23",
          "title": "Enforce Collection-Level Permissions in API",
          "description": "As the system, I want to enforce collection-level permissions on all document and query APIs, so that users only access authorized data",
          "epic": "epic-core-permissions-layer",
          "epicId": "f8082d2b-842e-4d99-8694-bff52e87c167",
          "priority": "high",
          "acceptanceCriteria": [
            "Functional: Users can only query documents in collections they are assigned to",
            "Functional: Upload and management APIs check user collection membership",
            "Technical: Permissions engine integrated into FastAPI middleware",
            "Technical: API returns 403 Forbidden for unauthorized access",
            "Technical: Permissions checks cover all relevant endpoints"
          ],
          "estimatedEffort": 20,
          "storyPoints": 8,
          "dependencies": [
            "42dd9560-1229-4fd2-b77c-0448d25409dd",
            "45f008df-44fb-4233-b644-e9858cd3b759",
            "e53e9568-7744-4ea0-b8bd-21f00bf99b30"
          ],
          "isSpike": false,
          "expectedOutcomes": [],
          "status": "approved",
          "llm_id": "us-011",
          "llmId": "us-011"
        },
        {
          "id": "42dd9560-1229-4fd2-b77c-0448d25409dd",
          "title": "Implement User Roles and Role Management",
          "description": "As an admin, I want to assign roles (admin, editor, viewer) to users, so that I can control their permissions",
          "epic": "epic-core-permissions-layer",
          "epicId": "f8082d2b-842e-4d99-8694-bff52e87c167",
          "priority": "high",
          "acceptanceCriteria": [
            "Functional: Admin can assign and change user roles",
            "Functional: Roles determine access rights in the system",
            "Technical: Roles and user_roles tables implemented in PostgreSQL",
            "Technical: API endpoints enforce role-based access control",
            "Technical: Frontend UI for role management"
          ],
          "estimatedEffort": 16,
          "storyPoints": 5,
          "dependencies": [
            "45f008df-44fb-4233-b644-e9858cd3b759"
          ],
          "isSpike": false,
          "expectedOutcomes": [],
          "status": "approved",
          "llm_id": "us-010",
          "llmId": "us-010"
        }
      ],
      "spikeStories": []
    },
    {
      "id": "3155fb16-86ee-412a-8d0b-40c58978d9a1",
      "title": "Document Upload and Management",
      "description": "This epic covers the features allowing admins and editors to upload documents, organize them into collections, and manage document metadata for efficient querying.",
      "stories": [
        {
          "id": "e7aa8ab6-008f-4b8c-8ad4-570257d5ca06",
          "title": "Allow Admins to Assign Users to Collections",
          "description": "As an admin, I want to assign users to document collections, so that I can control access to documents",
          "epic": "epic-core-document-upload-management",
          "epicId": "3155fb16-86ee-412a-8d0b-40c58978d9a1",
          "priority": "high",
          "acceptanceCriteria": [
            "Functional: Admin can assign and remove users from collections",
            "Functional: User collection assignments are enforced in permissions",
            "Technical: Assignments stored in user_collections table in PostgreSQL",
            "Technical: API endpoints for assignment enforce admin role",
            "Technical: Frontend UI for managing user assignments to collections"
          ],
          "estimatedEffort": 12,
          "storyPoints": 5,
          "dependencies": [
            "45f008df-44fb-4233-b644-e9858cd3b759",
            "42dd9560-1229-4fd2-b77c-0448d25409dd"
          ],
          "isSpike": false,
          "expectedOutcomes": [],
          "status": "approved",
          "llm_id": "us-009",
          "llmId": "us-009"
        },
        {
          "id": "e53e9568-7744-4ea0-b8bd-21f00bf99b30",
          "title": "Enable Editors to Upload and Manage Documents in Collections",
          "description": "As an editor, I want to upload documents into collections and manage them, so that I can maintain the knowledge base",
          "epic": "epic-core-document-upload-management",
          "epicId": "3155fb16-86ee-412a-8d0b-40c58978d9a1",
          "priority": "high",
          "acceptanceCriteria": [
            "Functional: Editors can upload documents to assigned collections",
            "Functional: Editors can view list of documents in collections",
            "Functional: Editors can delete documents they uploaded",
            "Technical: Upload API validates user role and collection membership",
            "Technical: Frontend document upload and management UI supports editors"
          ],
          "estimatedEffort": 20,
          "storyPoints": 8,
          "dependencies": [
            "45f008df-44fb-4233-b644-e9858cd3b759",
            "e4568bdb-c319-4ed5-8899-4c1d85757305"
          ],
          "isSpike": false,
          "expectedOutcomes": [],
          "status": "approved",
          "llm_id": "us-008",
          "llmId": "us-008"
        },
        {
          "id": "45f008df-44fb-4233-b644-e9858cd3b759",
          "title": "Implement Document Collections CRUD",
          "description": "As an admin, I want to create, read, update, and delete document collections, so that I can organize documents logically",
          "epic": "epic-core-document-upload-management",
          "epicId": "3155fb16-86ee-412a-8d0b-40c58978d9a1",
          "priority": "high",
          "acceptanceCriteria": [
            "Functional: Admin can create new collections with name and description",
            "Functional: Collections can be listed, updated, and deleted via API and frontend",
            "Technical: Collections stored in PostgreSQL with proper indexing",
            "Technical: API endpoints enforce admin/editor roles for collection management",
            "Technical: Frontend collection management UI implemented in React"
          ],
          "estimatedEffort": 16,
          "storyPoints": 5,
          "dependencies": [
            "e4568bdb-c319-4ed5-8899-4c1d85757305"
          ],
          "isSpike": false,
          "expectedOutcomes": [],
          "status": "approved",
          "llm_id": "us-007",
          "llmId": "us-007"
        }
      ],
      "spikeStories": []
    },
    {
      "id": "d00e5ae6-b1a2-4202-9dea-fc55127c51c2",
      "title": "Retrieval-Augmented Generation (RAG) Pipeline",
      "description": "This epic covers the implementation of the core RAG pipeline enabling users to upload documents and query them using natural language. It includes document ingestion, chunking, embedding generation, vector storage integration, local LLM inference, and answer generation with source citations.",
      "stories": [
        {
          "id": "b4a74558-170a-4610-8b22-0c51fefee1fa",
          "title": "Integrate Self-Hosted LLM Inference Using Ollama",
          "description": "As the system, I want to perform all LLM inference locally using Ollama, so that no data leaves the customer's infrastructure",
          "epic": "epic-core-rag-pipeline",
          "epicId": "d00e5ae6-b1a2-4202-9dea-fc55127c51c2",
          "priority": "high",
          "acceptanceCriteria": [
            "Functional: LLM inference requests are routed to local Ollama service",
            "Functional: No external API calls to third-party LLM providers occur",
            "Technical: Ollama is deployed as a Docker container and accessible via REST API",
            "Technical: Backend handles LLM prompt construction and response parsing",
            "Technical: LLM inference latency meets performance targets"
          ],
          "estimatedEffort": 16,
          "storyPoints": 5,
          "dependencies": [
            "f882cf33-6f83-48a9-b580-5fe62d87fa09"
          ],
          "isSpike": false,
          "expectedOutcomes": [],
          "status": "approved",
          "llm_id": "us-006",
          "llmId": "us-006"
        },
        {
          "id": "dae85381-58ba-45d8-a553-64209a750f2f",
          "title": "Implement Single-Turn Q&A Without Chat History",
          "description": "As a viewer, I want to perform single-turn queries without chat history, so that I can get immediate answers without session context",
          "epic": "epic-core-rag-pipeline",
          "epicId": "d00e5ae6-b1a2-4202-9dea-fc55127c51c2",
          "priority": "high",
          "acceptanceCriteria": [
            "Functional: Each query is independent with no stored conversation context",
            "Functional: System does not store or use previous queries for answer generation",
            "Technical: Backend query endpoint resets context per request",
            "Technical: No chat history data structures are maintained",
            "Technical: Frontend UI does not display or store chat history"
          ],
          "estimatedEffort": 8,
          "storyPoints": 3,
          "dependencies": [
            "f882cf33-6f83-48a9-b580-5fe62d87fa09"
          ],
          "isSpike": false,
          "expectedOutcomes": [],
          "status": "approved",
          "llm_id": "us-005",
          "llmId": "us-005"
        },
        {
          "id": "f882cf33-6f83-48a9-b580-5fe62d87fa09",
          "title": "Implement Natural Language Querying with RAG Pipeline",
          "description": "As a viewer, I want to enter natural language queries and receive plain English answers with source citations, so that I can quickly find relevant information",
          "epic": "epic-core-rag-pipeline",
          "epicId": "d00e5ae6-b1a2-4202-9dea-fc55127c51c2",
          "priority": "high",
          "acceptanceCriteria": [
            "Functional: User can submit a query via API and frontend search bar",
            "Functional: System returns an answer generated by local LLM with 2-3 source citations",
            "Functional: Citations link to original document chunks with snippet and page info",
            "Technical: Query handler retrieves top-k chunks from Qdrant based on embedding similarity",
            "Technical: LLM inference is performed locally using Ollama with prompt constructed from retrieved chunks"
          ],
          "estimatedEffort": 24,
          "storyPoints": 8,
          "dependencies": [
            "fbf00704-6f6c-466e-bf5a-1119edb5c9ba"
          ],
          "isSpike": false,
          "expectedOutcomes": [],
          "status": "approved",
          "llm_id": "us-004",
          "llmId": "us-004"
        },
        {
          "id": "fbf00704-6f6c-466e-bf5a-1119edb5c9ba",
          "title": "Generate Embeddings for Document Chunks and Store in Qdrant",
          "description": "As the system, I want to generate vector embeddings for document chunks and store them in Qdrant, so that semantic search queries can retrieve relevant chunks",
          "epic": "epic-core-rag-pipeline",
          "epicId": "d00e5ae6-b1a2-4202-9dea-fc55127c51c2",
          "priority": "high",
          "acceptanceCriteria": [
            "Functional: Embeddings are generated for all parsed chunks using local embedding model",
            "Functional: Embeddings are stored in Qdrant with metadata linking to document and chunk",
            "Technical: Embedding generation is batched and asynchronous",
            "Technical: Qdrant collections are created and indexed appropriately",
            "Technical: Embedding failures are logged and retried"
          ],
          "estimatedEffort": 20,
          "storyPoints": 8,
          "dependencies": [
            "87772124-3bce-4461-be87-8a0c4b2ed6a8"
          ],
          "isSpike": false,
          "expectedOutcomes": [],
          "status": "approved",
          "llm_id": "us-003",
          "llmId": "us-003"
        },
        {
          "id": "87772124-3bce-4461-be87-8a0c4b2ed6a8",
          "title": "Implement Document Parsing and Chunking for PDF and DOCX",
          "description": "As the system, I want to parse uploaded PDF and DOCX files into text chunks, so that they can be indexed for semantic search",
          "epic": "epic-core-rag-pipeline",
          "epicId": "d00e5ae6-b1a2-4202-9dea-fc55127c51c2",
          "priority": "high",
          "acceptanceCriteria": [
            "Functional: Uploaded documents are parsed into logical text chunks",
            "Functional: Each chunk is stored with metadata including document ID and chunk index",
            "Technical: Parsing supports page ranges and preserves text order",
            "Technical: Chunk data is stored in PostgreSQL document_chunks table",
            "Technical: Parsing process is asynchronous and reports status"
          ],
          "estimatedEffort": 20,
          "storyPoints": 8,
          "dependencies": [
            "e4568bdb-c319-4ed5-8899-4c1d85757305"
          ],
          "isSpike": false,
          "expectedOutcomes": [],
          "status": "approved",
          "llm_id": "us-002",
          "llmId": "us-002"
        },
        {
          "id": "e4568bdb-c319-4ed5-8899-4c1d85757305",
          "title": "Implement Document Upload Support for PDF and DOCX",
          "description": "As an editor, I want to upload PDF and DOCX documents, so that I can add knowledge sources to the system",
          "epic": "epic-core-rag-pipeline",
          "epicId": "d00e5ae6-b1a2-4202-9dea-fc55127c51c2",
          "priority": "high",
          "acceptanceCriteria": [
            "Functional: Editor can upload PDF and DOCX files via API and frontend",
            "Functional: Uploaded files are stored securely in file storage",
            "Technical: Backend validates file type and size before accepting upload",
            "Technical: Files are saved with unique identifiers and metadata stored in PostgreSQL",
            "Technical: Upload endpoint returns success status and document metadata"
          ],
          "estimatedEffort": 16,
          "storyPoints": 5,
          "dependencies": [],
          "isSpike": false,
          "expectedOutcomes": [],
          "status": "approved",
          "llm_id": "us-001",
          "llmId": "us-001"
        }
      ],
      "spikeStories": []
    }
  ],
  "stories": [],
  "spikeStories": [
    {
      "id": "88817ee0-4ab5-471d-b15e-a9f4d4f5bb5a",
      "title": "Spike: Plan Document-Level Permissions for Future Release",
      "description": "As the system architect, I want to design document-level permissions for v2, so that finer-grained access control can be implemented later",
      "priority": "medium",
      "acceptanceCriteria": [
        "Design documented",
        "Roadmap created"
      ],
      "storyPoints": 5,
      "dependencies": [],
      "isSpike": true,
      "timebox": "4 days",
      "expectedOutcomes": [
        "Design document-level permission model documented",
        "Data schema extensions proposed for document-level ACLs",
        "API design for document-level permission management drafted",
        "Security implications and compliance considerations analyzed",
        "Implementation plan and roadmap created"
      ],
      "status": "approved",
      "llm_id": "spike-033",
      "llmId": "spike-033"
    },
    {
      "id": "a69a3dca-0889-4b1b-8e8c-6cf1609e2266",
      "title": "Spike: Design API Connectors for External Document Sources (Post-Launch)",
      "description": "As a developer, I want to research and design API connectors for Confluence, Notion, Google Drive, and SharePoint, so that future versions can import documents from these sources",
      "priority": "medium",
      "acceptanceCriteria": [
        "Research completed",
        "Documentation provided"
      ],
      "storyPoints": 8,
      "dependencies": [],
      "isSpike": true,
      "timebox": "1 week",
      "expectedOutcomes": [
        "Research completed for each external API's authentication and data retrieval",
        "Design documented for connector architecture and integration points",
        "Proof-of-concept code snippets or SDK usage examples provided",
        "Integration challenges and limitations identified",
        "Recommendations for phased implementation prioritized"
      ],
      "status": "approved",
      "llm_id": "spike-025",
      "llmId": "spike-025"
    }
  ],
  "userStories": [
    {
      "id": "88817ee0-4ab5-471d-b15e-a9f4d4f5bb5a",
      "title": "Spike: Plan Document-Level Permissions for Future Release",
      "description": "As the system architect, I want to design document-level permissions for v2, so that finer-grained access control can be implemented later",
      "priority": "medium",
      "acceptanceCriteria": [
        "Design documented",
        "Roadmap created"
      ],
      "storyPoints": 5,
      "dependencies": [],
      "isSpike": true,
      "timebox": "4 days",
      "expectedOutcomes": [
        "Design document-level permission model documented",
        "Data schema extensions proposed for document-level ACLs",
        "API design for document-level permission management drafted",
        "Security implications and compliance considerations analyzed",
        "Implementation plan and roadmap created"
      ],
      "status": "approved",
      "llm_id": "spike-033",
      "llmId": "spike-033"
    },
    {
      "id": "a69a3dca-0889-4b1b-8e8c-6cf1609e2266",
      "title": "Spike: Design API Connectors for External Document Sources (Post-Launch)",
      "description": "As a developer, I want to research and design API connectors for Confluence, Notion, Google Drive, and SharePoint, so that future versions can import documents from these sources",
      "priority": "medium",
      "acceptanceCriteria": [
        "Research completed",
        "Documentation provided"
      ],
      "storyPoints": 8,
      "dependencies": [],
      "isSpike": true,
      "timebox": "1 week",
      "expectedOutcomes": [
        "Research completed for each external API's authentication and data retrieval",
        "Design documented for connector architecture and integration points",
        "Proof-of-concept code snippets or SDK usage examples provided",
        "Integration challenges and limitations identified",
        "Recommendations for phased implementation prioritized"
      ],
      "status": "approved",
      "llm_id": "spike-025",
      "llmId": "spike-025"
    },
    {
      "id": "d6969e05-a00f-4a1e-88ee-03c58c588672",
      "title": "Spike: Documentation Framework Setup",
      "description": "As the solo developer, I need to set up documentation frameworks for API docs and user guides, so that documentation is maintained and accessible",
      "epic": "epic-infrastructure-initial-setup",
      "epicId": "1e94200a-d976-4f0f-8dd1-ba87882580d2",
      "priority": "high",
      "acceptanceCriteria": [
        "API docs accessible via /docs endpoint",
        "User and developer documentation is version-controlled",
        "Documentation build process automated"
      ],
      "storyPoints": 3,
      "dependencies": [],
      "isSpike": true,
      "timebox": "3 days",
      "expectedOutcomes": [
        "OpenAPI docs generated automatically from FastAPI",
        "User guides and developer docs organized in markdown",
        "Documentation site or README structure established"
      ],
      "status": "approved",
      "llm_id": "spike-007",
      "llmId": "spike-007"
    },
    {
      "id": "1dd895d2-912d-4b6d-b4bf-9ec4b960d8d4",
      "title": "Spike: Code Quality Tools Setup",
      "description": "As the solo developer, I need to set up code quality tools like ESLint, Prettier, and Python linters, so that code style and quality are enforced",
      "epic": "epic-infrastructure-initial-setup",
      "epicId": "1e94200a-d976-4f0f-8dd1-ba87882580d2",
      "priority": "high",
      "acceptanceCriteria": [
        "Code style violations are detected during development and CI",
        "Pre-commit hooks prevent bad commits",
        "Code quality rules documented"
      ],
      "storyPoints": 2,
      "dependencies": [],
      "isSpike": true,
      "timebox": "2 days",
      "expectedOutcomes": [
        "ESLint and Prettier configured for frontend",
        "Flake8 or pylint configured for backend",
        "Pre-commit hooks set up for formatting and linting"
      ],
      "status": "approved",
      "llm_id": "spike-006",
      "llmId": "spike-006"
    },
    {
      "id": "6992f866-ffc3-4077-bec3-6e5e0f754826",
      "title": "Spike: Testing Framework Setup",
      "description": "As the solo developer, I need to set up testing frameworks for backend and frontend, so that automated tests can be written and run",
      "epic": "epic-infrastructure-initial-setup",
      "epicId": "1e94200a-d976-4f0f-8dd1-ba87882580d2",
      "priority": "high",
      "acceptanceCriteria": [
        "Tests can be run locally and in CI",
        "Sample tests demonstrate framework usage",
        "Test failures cause CI pipeline to fail"
      ],
      "storyPoints": 3,
      "dependencies": [],
      "isSpike": true,
      "timebox": "3 days",
      "expectedOutcomes": [
        "Backend unit testing with pytest configured",
        "Frontend testing with Jest and React Testing Library",
        "Test coverage reports generated"
      ],
      "status": "approved",
      "llm_id": "spike-005",
      "llmId": "spike-005"
    },
    {
      "id": "a5624a29-7263-4ac7-9b78-b45dffab2ac2",
      "title": "Spike: Database Migration Framework Setup",
      "description": "As the solo developer, I need to set up a database migration framework for PostgreSQL, so that schema changes can be managed safely",
      "epic": "epic-infrastructure-initial-setup",
      "epicId": "1e94200a-d976-4f0f-8dd1-ba87882580d2",
      "priority": "high",
      "acceptanceCriteria": [
        "Migrations can be applied and rolled back locally",
        "Migration scripts version-controlled",
        "Migration process documented"
      ],
      "storyPoints": 3,
      "dependencies": [],
      "isSpike": true,
      "timebox": "2 days",
      "expectedOutcomes": [
        "Migration tool integrated (e.g., Alembic)",
        "Initial migration scripts created for base schema",
        "Migration commands documented"
      ],
      "status": "approved",
      "llm_id": "spike-004",
      "llmId": "spike-004"
    },
    {
      "id": "87192e9f-a90b-4114-86b1-649417beb60a",
      "title": "Spike: CI/CD Pipeline Setup with GitHub Actions",
      "description": "As the solo developer, I need to set up CI/CD pipelines for linting, testing, and building Docker images, so that code quality and deployment are automated",
      "epic": "epic-infrastructure-initial-setup",
      "epicId": "1e94200a-d976-4f0f-8dd1-ba87882580d2",
      "priority": "high",
      "acceptanceCriteria": [
        "CI pipeline runs on every PR and commit",
        "Linting and tests must pass before merge",
        "Docker images are built and tagged correctly"
      ],
      "storyPoints": 5,
      "dependencies": [],
      "isSpike": true,
      "timebox": "4 days",
      "expectedOutcomes": [
        "GitHub Actions workflows for linting and unit tests",
        "Docker image build and push steps",
        "Automated test runs on pull requests"
      ],
      "status": "approved",
      "llm_id": "spike-003",
      "llmId": "spike-003"
    },
    {
      "id": "8c8179ab-d0ed-4e33-939f-3605fd9dccc6",
      "title": "Spike: Development Environment Setup",
      "description": "As the solo developer, I need to set up local development environments including Docker Compose, Python virtualenv, and React tooling, so that I can develop and test efficiently",
      "epic": "epic-infrastructure-initial-setup",
      "epicId": "1e94200a-d976-4f0f-8dd1-ba87882580d2",
      "priority": "high",
      "acceptanceCriteria": [
        "Local dev environment can be started with a single command",
        "Code changes reflect immediately in running containers",
        "Linting and formatting tools are configured"
      ],
      "storyPoints": 3,
      "dependencies": [],
      "isSpike": true,
      "timebox": "3 days",
      "expectedOutcomes": [
        "Docker Compose environment for local dev with hot reload",
        "Python backend environment with dependencies and linting",
        "React frontend environment with build and test scripts"
      ],
      "status": "approved",
      "llm_id": "spike-002",
      "llmId": "spike-002"
    },
    {
      "id": "d0988cff-8588-4821-b6bc-4f0a8a9d7147",
      "title": "Spike: Repository Initialization and Project Scaffolding",
      "description": "As the solo developer, I need to set up the monorepo structure and initial project scaffolding, so that development can proceed efficiently",
      "epic": "epic-infrastructure-initial-setup",
      "epicId": "1e94200a-d976-4f0f-8dd1-ba87882580d2",
      "priority": "high",
      "acceptanceCriteria": [
        "Repository initialized with monorepo structure",
        "Basic README and contribution guidelines added",
        "Docker Compose file includes placeholders for services"
      ],
      "storyPoints": 3,
      "dependencies": [],
      "isSpike": true,
      "timebox": "3 days",
      "expectedOutcomes": [
        "Monorepo with backend, frontend, and infrastructure directories",
        "Basic project structure with initial files and README",
        "Initial Dockerfiles and docker-compose.yml stub"
      ],
      "status": "approved",
      "llm_id": "spike-001",
      "llmId": "spike-001"
    },
    {
      "id": "1335140c-c61d-444f-bad1-76d05d49b0ed",
      "title": "Ensure First Query Setup Completes Within 10 Minutes",
      "description": "As an admin, I want to complete initial setup and run the first query within 10 minutes, so that onboarding is efficient",
      "epic": "epic-nfr-usability-accessibility-error-handling",
      "epicId": "978d9d0a-fc04-411d-aca0-0755eddf1d11",
      "priority": "high",
      "acceptanceCriteria": [
        "Functional: Setup wizard guides admin through workspace creation, document upload, and user assignment",
        "Functional: System provides progress indicators and tooltips",
        "Technical: Backend APIs respond quickly to setup requests",
        "Technical: Frontend UI optimized for quick navigation",
        "Technical: User feedback collected during pilot to validate timing"
      ],
      "estimatedEffort": 16,
      "storyPoints": 5,
      "dependencies": [
        "6208c1c5-76b6-4e31-a61a-774d544c7904",
        "f13817a7-d052-435f-9af4-d18438923327",
        "0b71d701-32b4-4653-815a-141f65c0ab36"
      ],
      "isSpike": false,
      "expectedOutcomes": [],
      "status": "approved",
      "llm_id": "us-043",
      "llmId": "us-043"
    },
    {
      "id": "0d7ea346-b931-4d35-b080-6581bb1c6caa",
      "title": "Provide Clear Error Messages and User Feedback",
      "description": "As a user, I want clear and actionable error messages, so that I can understand and resolve issues quickly",
      "epic": "epic-nfr-usability-accessibility-error-handling",
      "epicId": "978d9d0a-fc04-411d-aca0-0755eddf1d11",
      "priority": "high",
      "acceptanceCriteria": [
        "Functional: UI displays user-friendly error messages for common failures",
        "Functional: API returns standardized error codes and messages",
        "Technical: Frontend maps API errors to UI notifications",
        "Technical: Validation errors highlight specific input fields",
        "Technical: Error messages are logged for diagnostics"
      ],
      "estimatedEffort": 12,
      "storyPoints": 3,
      "dependencies": [
        "8492a709-2452-4f86-9abc-6e327ce60924",
        "62bd29d4-0f85-4ea8-b4f8-72745aab041d",
        "0b71d701-32b4-4653-815a-141f65c0ab36"
      ],
      "isSpike": false,
      "expectedOutcomes": [],
      "status": "approved",
      "llm_id": "us-042",
      "llmId": "us-042"
    },
    {
      "id": "45bc1336-5e4e-4faf-9370-389840a9dea6",
      "title": "Implement Accessible Frontend UI Components",
      "description": "As a knowledge worker, I want the UI to be accessible and compliant with WCAG 2.1 AA, so that I can use the system regardless of disabilities",
      "epic": "epic-nfr-usability-accessibility-error-handling",
      "epicId": "978d9d0a-fc04-411d-aca0-0755eddf1d11",
      "priority": "high",
      "acceptanceCriteria": [
        "Functional: UI components support keyboard navigation and screen readers",
        "Functional: Color contrast meets WCAG 2.1 AA standards",
        "Technical: Use Chakra UI accessibility features",
        "Technical: Accessibility tests performed with automated tools",
        "Technical: Accessibility issues fixed before release"
      ],
      "estimatedEffort": 16,
      "storyPoints": 5,
      "dependencies": [
        "6208c1c5-76b6-4e31-a61a-774d544c7904",
        "0b71d701-32b4-4653-815a-141f65c0ab36"
      ],
      "isSpike": false,
      "expectedOutcomes": [],
      "status": "approved",
      "llm_id": "us-041",
      "llmId": "us-041"
    },
    {
      "id": "59b96aa7-bb5c-4018-9e9b-3dbc5c324c47",
      "title": "Provide Backup and Restore Procedures and Scripts",
      "description": "As a system administrator, I want documented backup and restore procedures and scripts, so that I can recover data in case of disaster",
      "epic": "epic-nfr-reliability-uptime-disaster-recovery",
      "epicId": "c1c888c6-926d-45a9-b821-b73b5523f921",
      "priority": "high",
      "acceptanceCriteria": [
        "Functional: Backup scripts export PostgreSQL data and file storage safely",
        "Functional: Restore scripts can recover system state from backups",
        "Technical: Qdrant snapshot and restore procedures documented",
        "Technical: Backup and restore tested end-to-end",
        "Technical: Documentation includes scheduling and verification steps"
      ],
      "estimatedEffort": 16,
      "storyPoints": 5,
      "dependencies": [
        "04a4eaea-8fa2-4d42-b43c-0dcd1c091cd1"
      ],
      "isSpike": false,
      "expectedOutcomes": [],
      "status": "approved",
      "llm_id": "us-040",
      "llmId": "us-040"
    },
    {
      "id": "0212c747-3a2f-4ab1-9669-3ff5606b978b",
      "title": "Implement Graceful Error Handling and Recovery",
      "description": "As the system, I want to handle errors gracefully and recover from failures without data loss, so that uptime and reliability are maximized",
      "epic": "epic-nfr-reliability-uptime-disaster-recovery",
      "epicId": "c1c888c6-926d-45a9-b821-b73b5523f921",
      "priority": "high",
      "acceptanceCriteria": [
        "Functional: API returns standardized error responses with meaningful messages",
        "Functional: System retries transient failures where appropriate",
        "Technical: Unhandled exceptions are logged and do not crash services",
        "Technical: Services restart automatically on failure in Docker Compose",
        "Technical: Health endpoints report service status accurately"
      ],
      "estimatedEffort": 12,
      "storyPoints": 5,
      "dependencies": [
        "8492a709-2452-4f86-9abc-6e327ce60924",
        "62bd29d4-0f85-4ea8-b4f8-72745aab041d",
        "9d9a1745-8f55-42e4-b237-0f5efd391741",
        "04a4eaea-8fa2-4d42-b43c-0dcd1c091cd1"
      ],
      "isSpike": false,
      "expectedOutcomes": [],
      "status": "approved",
      "llm_id": "us-039",
      "llmId": "us-039"
    },
    {
      "id": "54f04eec-eb67-44c6-9b63-9296b9246396",
      "title": "Set Up Metrics Collection and Alerting",
      "description": "As the system, I want to collect metrics like query latency, upload success, and error rates, and configure alerts, so that system health is monitored proactively",
      "epic": "epic-nfr-monitoring-logging-alerts",
      "epicId": "fc9782b9-5ac2-4b91-b4fa-9c35c874401a",
      "priority": "medium",
      "acceptanceCriteria": [
        "Functional: Metrics are collected and exposed via Prometheus endpoints",
        "Functional: Alerts are configured for failed uploads, permission errors, and high latency",
        "Technical: Grafana dashboards created for key metrics",
        "Technical: Alert notifications sent to configured channels",
        "Technical: Monitoring components deployed in Docker Compose"
      ],
      "estimatedEffort": 16,
      "storyPoints": 5,
      "dependencies": [
        "04a4eaea-8fa2-4d42-b43c-0dcd1c091cd1"
      ],
      "isSpike": false,
      "expectedOutcomes": [],
      "status": "approved",
      "llm_id": "us-038",
      "llmId": "us-038"
    },
    {
      "id": "357fdd09-4a93-4edc-89fb-feb7aba83f9a",
      "title": "Implement Structured Logging for Backend Services",
      "description": "As the system, I want to implement structured logging with appropriate levels and context, so that issues can be diagnosed efficiently",
      "epic": "epic-nfr-monitoring-logging-alerts",
      "epicId": "fc9782b9-5ac2-4b91-b4fa-9c35c874401a",
      "priority": "high",
      "acceptanceCriteria": [
        "Functional: All API calls, ingestion, and query events are logged with structured JSON format",
        "Technical: Logs include timestamps, user IDs, request IDs, and error details",
        "Technical: Sensitive data is excluded from logs",
        "Technical: Logs are written to stdout and file with rotation",
        "Technical: Logging configuration supports level adjustment"
      ],
      "estimatedEffort": 12,
      "storyPoints": 5,
      "dependencies": [
        "8492a709-2452-4f86-9abc-6e327ce60924",
        "62bd29d4-0f85-4ea8-b4f8-72745aab041d",
        "9d9a1745-8f55-42e4-b237-0f5efd391741"
      ],
      "isSpike": false,
      "expectedOutcomes": [],
      "status": "approved",
      "llm_id": "us-037",
      "llmId": "us-037"
    },
    {
      "id": "9bf767df-c5e6-44f9-8d1f-257f72c4f7fc",
      "title": "Use Open-Source Backend and Frontend Frameworks",
      "description": "As the system architect, I want to use open-source frameworks like FastAPI, React, Qdrant, and Ollama, so that the system remains transparent and vendor-neutral",
      "epic": "epic-nfr-open-source-component-usage",
      "epicId": "4f341213-9613-4bae-887e-da48eca79d46",
      "priority": "high",
      "acceptanceCriteria": [
        "Functional: All core components use open-source licenses",
        "Technical: No proprietary or opinionated libraries like LangChain are used",
        "Technical: Custom RAG pipeline implemented without third-party abstraction layers",
        "Technical: Dependencies are documented and regularly audited",
        "Technical: Community-supported versions of components are used"
      ],
      "estimatedEffort": 8,
      "storyPoints": 3,
      "dependencies": [],
      "isSpike": false,
      "expectedOutcomes": [],
      "status": "approved",
      "llm_id": "us-036",
      "llmId": "us-036"
    },
    {
      "id": "f3a09f78-2f24-4cd6-8f65-a205c23058d5",
      "title": "Implement Backend Performance Tuning and Monitoring",
      "description": "As the system, I want to tune backend performance and monitor key metrics to maintain smooth user experience",
      "epic": "epic-nfr-performance-latency",
      "epicId": "7abab78f-dd94-44bd-9569-eee8992e8d8b",
      "priority": "high",
      "acceptanceCriteria": [
        "Functional: Backend APIs respond within target times under load",
        "Technical: Database connection pooling configured",
        "Technical: API rate limiting implemented",
        "Technical: Metrics collected for response times and error rates",
        "Technical: Alerts configured for performance degradation"
      ],
      "estimatedEffort": 16,
      "storyPoints": 5,
      "dependencies": [
        "8492a709-2452-4f86-9abc-6e327ce60924",
        "62bd29d4-0f85-4ea8-b4f8-72745aab041d",
        "9d9a1745-8f55-42e4-b237-0f5efd391741"
      ],
      "isSpike": false,
      "expectedOutcomes": [],
      "status": "approved",
      "llm_id": "us-035",
      "llmId": "us-035"
    },
    {
      "id": "de91b0cd-2593-4b5d-bf67-9b93ad16cb34",
      "title": "Optimize RAG Pipeline for Low Latency",
      "description": "As the system, I want to optimize the RAG pipeline components to ensure query response latency is under 3 seconds at 95th percentile",
      "epic": "epic-nfr-performance-latency",
      "epicId": "7abab78f-dd94-44bd-9569-eee8992e8d8b",
      "priority": "high",
      "acceptanceCriteria": [
        "Functional: Query response times measured and meet latency targets",
        "Technical: Pipeline components are profiled and bottlenecks identified",
        "Technical: Parallelization or caching applied where beneficial",
        "Technical: Load testing simulates expected query volumes",
        "Technical: Monitoring metrics collected for latency"
      ],
      "estimatedEffort": 20,
      "storyPoints": 8,
      "dependencies": [
        "f882cf33-6f83-48a9-b580-5fe62d87fa09",
        "203cf20a-c961-4ad7-a28b-813eca8fd4b5",
        "b2731712-f394-470f-a017-f4d0d2f1b27b"
      ],
      "isSpike": false,
      "expectedOutcomes": [],
      "status": "approved",
      "llm_id": "us-034",
      "llmId": "us-034"
    },
    {
      "id": "ec45289b-a5b2-4cee-856a-fcdca5b2d616",
      "title": "Plan Document-Level Permissions for Future Release",
      "description": "As the system architect, I want to design document-level permissions for v2, so that finer-grained access control can be implemented later",
      "epic": "epic-nfr-data-security-access-control",
      "epicId": "8c011662-b385-416b-9fd3-7cdf12293fc4",
      "priority": "medium",
      "acceptanceCriteria": [
        "Design document-level permission model documented",
        "Data schema extensions proposed for document-level ACLs",
        "API design for document-level permission management drafted",
        "Security implications and compliance considerations analyzed",
        "Implementation plan and roadmap created"
      ],
      "estimatedEffort": 16,
      "storyPoints": 5,
      "dependencies": [],
      "isSpike": false,
      "expectedOutcomes": [],
      "status": "approved",
      "llm_id": "us-033",
      "llmId": "us-033"
    },
    {
      "id": "83204155-76db-4820-8d5d-f90272d0f39c",
      "title": "Integrate Enterprise SSO for Secure Authentication",
      "description": "As an enterprise user, I want to authenticate securely via SAML/OIDC SSO, so that access complies with corporate security policies",
      "epic": "epic-nfr-data-security-access-control",
      "epicId": "8c011662-b385-416b-9fd3-7cdf12293fc4",
      "priority": "high",
      "acceptanceCriteria": [
        "Functional: SSO login supports major IdPs like Okta, Azure AD, Google Workspace",
        "Functional: Authentication tokens are securely handled and validated",
        "Technical: Use secure session management and JWT signing",
        "Technical: SSO configurations are encrypted and stored securely",
        "Technical: Audit logs record all authentication events"
      ],
      "estimatedEffort": 24,
      "storyPoints": 8,
      "dependencies": [
        "4bc93892-023b-460f-adc3-a7179c81b722",
        "9cb4b78a-4931-4001-a971-c41d0bd03860",
        "16d112e4-ae39-4d67-bf88-5fc6be123d36"
      ],
      "isSpike": false,
      "expectedOutcomes": [],
      "status": "approved",
      "llm_id": "us-032",
      "llmId": "us-032"
    },
    {
      "id": "41b28af8-b288-4441-a849-975a2794a104",
      "title": "Enforce Collection-Level Permissions in API and Query Layer",
      "description": "As the system, I want to enforce collection-level permissions on all API and query operations, so that users only access authorized documents",
      "epic": "epic-nfr-data-security-access-control",
      "epicId": "8c011662-b385-416b-9fd3-7cdf12293fc4",
      "priority": "high",
      "acceptanceCriteria": [
        "Functional: API returns 403 Forbidden for unauthorized collection access",
        "Functional: Query results only include documents from permitted collections",
        "Technical: Permissions checks integrated in API middleware and query handlers",
        "Technical: Unit and integration tests cover permission enforcement",
        "Technical: Audit logs record permission violations"
      ],
      "estimatedEffort": 20,
      "storyPoints": 8,
      "dependencies": [
        "a23bb700-bd6a-4d83-8229-e926c0733b23"
      ],
      "isSpike": false,
      "expectedOutcomes": [],
      "status": "approved",
      "llm_id": "us-031",
      "llmId": "us-031"
    },
    {
      "id": "ca7a6981-1f47-4709-9992-2cfcaacb9fff",
      "title": "Implement Database Indexing and Query Optimization",
      "description": "As the system, I want to optimize PostgreSQL database indexes and queries to support large user and document volumes efficiently",
      "epic": "epic-infrastructure-scalability",
      "epicId": "48a8a9b1-8722-4db3-b976-dd401b90964a",
      "priority": "medium",
      "acceptanceCriteria": [
        "Functional: Database queries for user, document, and collection data are performant",
        "Technical: Indexes created on frequently queried columns",
        "Technical: Query plans analyzed and optimized",
        "Technical: Database connection pooling configured",
        "Technical: Performance tests validate query response times"
      ],
      "estimatedEffort": 16,
      "storyPoints": 5,
      "dependencies": [
        "45f008df-44fb-4233-b644-e9858cd3b759",
        "42dd9560-1229-4fd2-b77c-0448d25409dd"
      ],
      "isSpike": false,
      "expectedOutcomes": [],
      "status": "approved",
      "llm_id": "us-030",
      "llmId": "us-030"
    },
    {
      "id": "b2731712-f394-470f-a017-f4d0d2f1b27b",
      "title": "Optimize Local LLM Inference Performance",
      "description": "As the system, I want to optimize Ollama LLM inference performance to support up to 500 queries per day per organization with low latency",
      "epic": "epic-infrastructure-scalability",
      "epicId": "48a8a9b1-8722-4db3-b976-dd401b90964a",
      "priority": "medium",
      "acceptanceCriteria": [
        "Functional: LLM inference latency measured and optimized",
        "Technical: Model quantization or size configuration supported",
        "Technical: Resource usage monitored and optimized",
        "Technical: Failover or retry logic implemented for LLM errors",
        "Technical: Performance tests validate throughput targets"
      ],
      "estimatedEffort": 16,
      "storyPoints": 5,
      "dependencies": [
        "b4a74558-170a-4610-8b22-0c51fefee1fa"
      ],
      "isSpike": false,
      "expectedOutcomes": [],
      "status": "approved",
      "llm_id": "us-029",
      "llmId": "us-029"
    },
    {
      "id": "203cf20a-c961-4ad7-a28b-813eca8fd4b5",
      "title": "Optimize Vector Search Performance with Qdrant",
      "description": "As the system, I want to optimize Qdrant vector search performance to handle up to 50,000 documents per organization, so that query latency remains under 3 seconds",
      "epic": "epic-infrastructure-scalability",
      "epicId": "48a8a9b1-8722-4db3-b976-dd401b90964a",
      "priority": "medium",
      "acceptanceCriteria": [
        "Functional: Vector search latency measured and optimized under load",
        "Technical: Qdrant indexing parameters tuned for large datasets",
        "Technical: Query caching or batching strategies evaluated",
        "Technical: Performance tests simulate target query volumes",
        "Technical: Monitoring metrics collected for query latency"
      ],
      "estimatedEffort": 20,
      "storyPoints": 8,
      "dependencies": [
        "fbf00704-6f6c-466e-bf5a-1119edb5c9ba"
      ],
      "isSpike": false,
      "expectedOutcomes": [],
      "status": "approved",
      "llm_id": "us-028",
      "llmId": "us-028"
    },
    {
      "id": "d47e24b1-bc42-4a25-a9c0-5056a6850178",
      "title": "Document Installation and Operation Guide for Self-Hosted Deployment",
      "description": "As a customer, I want clear documentation on how to install, configure, and operate the system using Docker Compose, so that I can deploy and maintain it successfully",
      "epic": "epic-infrastructure-self-hosted-deployment",
      "epicId": "d01b1200-7fb4-461a-a21d-aeff2664f63c",
      "priority": "high",
      "acceptanceCriteria": [
        "Functional: Documentation covers prerequisites, installation steps, and configuration",
        "Functional: Troubleshooting and common issues are described",
        "Technical: Instructions include environment variable setup and secret management",
        "Technical: Guide includes backup and restore procedures",
        "Technical: Documentation is accessible in the repository and website"
      ],
      "estimatedEffort": 12,
      "storyPoints": 3,
      "dependencies": [
        "04a4eaea-8fa2-4d42-b43c-0dcd1c091cd1"
      ],
      "isSpike": false,
      "expectedOutcomes": [],
      "status": "approved",
      "llm_id": "us-027",
      "llmId": "us-027"
    },
    {
      "id": "04a4eaea-8fa2-4d42-b43c-0dcd1c091cd1",
      "title": "Create Docker Compose Configuration for All Components",
      "description": "As the system, I want to provide a Docker Compose configuration that orchestrates backend, frontend, Qdrant, Ollama, and PostgreSQL, so that customers can deploy the system easily",
      "epic": "epic-infrastructure-self-hosted-deployment",
      "epicId": "d01b1200-7fb4-461a-a21d-aeff2664f63c",
      "priority": "high",
      "acceptanceCriteria": [
        "Functional: Docker Compose file defines all required services with correct networking",
        "Functional: Services start and communicate correctly on a single host",
        "Technical: Persistent volumes configured for data storage",
        "Technical: Environment variables and secrets managed securely",
        "Technical: Compose file supports configuration overrides"
      ],
      "estimatedEffort": 16,
      "storyPoints": 5,
      "dependencies": [],
      "isSpike": false,
      "expectedOutcomes": [],
      "status": "approved",
      "llm_id": "us-026",
      "llmId": "us-026"
    },
    {
      "id": "92806d55-ac0d-4cda-94e9-f9f33c5fd0b2",
      "title": "Design API Connectors for External Document Sources (Post-Launch Spike)",
      "description": "As a developer, I want to research and design API connectors for Confluence, Notion, Google Drive, and SharePoint, so that future versions can import documents from these sources",
      "epic": "epic-integration-file-upload-support",
      "epicId": "f1e1cc77-d778-46af-8e1e-ec8676f2f989",
      "priority": "medium",
      "acceptanceCriteria": [
        "Research completed for each external API's authentication and data retrieval",
        "Design documented for connector architecture and integration points",
        "Proof-of-concept code snippets or SDK usage examples provided",
        "Integration challenges and limitations identified",
        "Recommendations for phased implementation prioritized"
      ],
      "estimatedEffort": 24,
      "storyPoints": 8,
      "dependencies": [],
      "isSpike": false,
      "expectedOutcomes": [],
      "status": "approved",
      "llm_id": "us-025",
      "llmId": "us-025"
    },
    {
      "id": "dc5cef48-815b-4348-baea-08b9b539f45e",
      "title": "Support File Uploads for PDF, DOCX, and TXT Formats",
      "description": "As an editor, I want to upload PDF, DOCX, and TXT files, so that I can add diverse document types to the knowledge base",
      "epic": "epic-integration-file-upload-support",
      "epicId": "f1e1cc77-d778-46af-8e1e-ec8676f2f989",
      "priority": "high",
      "acceptanceCriteria": [
        "Functional: System accepts PDF, DOCX, and TXT files via upload API",
        "Functional: Files are validated for type and size before acceptance",
        "Technical: Backend uses file parsing libraries for all three formats",
        "Technical: Uploaded files are stored and indexed correctly",
        "Technical: Frontend upload UI supports all three file types"
      ],
      "estimatedEffort": 16,
      "storyPoints": 5,
      "dependencies": [
        "e4568bdb-c319-4ed5-8899-4c1d85757305",
        "87772124-3bce-4461-be87-8a0c4b2ed6a8"
      ],
      "isSpike": false,
      "expectedOutcomes": [],
      "status": "approved",
      "llm_id": "us-024",
      "llmId": "us-024"
    },
    {
      "id": "4e9cef6c-7a55-4e5a-8097-2cd159a4027b",
      "title": "Integrate SSO Authentication with User and Permission Management",
      "description": "As the system, I want to link SSO authenticated users with internal user roles and collection assignments, so that permissions are enforced correctly",
      "epic": "epic-integration-sso",
      "epicId": "bf4bfece-d2fd-4d9a-8fc9-a7d83f781c2b",
      "priority": "high",
      "acceptanceCriteria": [
        "Functional: SSO login creates or links user accounts in PostgreSQL",
        "Functional: User roles and collection assignments are loaded post-login",
        "Technical: JWT tokens include user roles and collection claims",
        "Technical: Permissions engine uses SSO user identity for access control",
        "Technical: Audit logs record SSO login events"
      ],
      "estimatedEffort": 16,
      "storyPoints": 5,
      "dependencies": [
        "9cb4b78a-4931-4001-a971-c41d0bd03860",
        "16d112e4-ae39-4d67-bf88-5fc6be123d36",
        "42dd9560-1229-4fd2-b77c-0448d25409dd",
        "a23bb700-bd6a-4d83-8229-e926c0733b23"
      ],
      "isSpike": false,
      "expectedOutcomes": [],
      "status": "approved",
      "llm_id": "us-023",
      "llmId": "us-023"
    },
    {
      "id": "16d112e4-ae39-4d67-bf88-5fc6be123d36",
      "title": "Implement OIDC Authentication Flow",
      "description": "As an enterprise user, I want to authenticate via OIDC SSO, so that I can securely access the system using my corporate credentials",
      "epic": "epic-integration-sso",
      "epicId": "bf4bfece-d2fd-4d9a-8fc9-a7d83f781c2b",
      "priority": "high",
      "acceptanceCriteria": [
        "Functional: System supports OIDC authorization code flow with major IdPs",
        "Functional: System exchanges code for tokens and validates ID token",
        "Technical: Use Authlib library for OIDC protocol handling",
        "Technical: OIDC client configuration is per organization",
        "Technical: Tokens stored securely and used for session management"
      ],
      "estimatedEffort": 24,
      "storyPoints": 8,
      "dependencies": [],
      "isSpike": false,
      "expectedOutcomes": [],
      "status": "approved",
      "llm_id": "us-022",
      "llmId": "us-022"
    },
    {
      "id": "9cb4b78a-4931-4001-a971-c41d0bd03860",
      "title": "Implement SAML Authentication Flow",
      "description": "As an enterprise user, I want to authenticate via SAML SSO, so that I can securely access the system using my corporate credentials",
      "epic": "epic-integration-sso",
      "epicId": "bf4bfece-d2fd-4d9a-8fc9-a7d83f781c2b",
      "priority": "high",
      "acceptanceCriteria": [
        "Functional: System initiates SAML authentication with configured IdP",
        "Functional: System processes SAML assertions and creates user sessions",
        "Technical: Use python-saml library for SAML protocol handling",
        "Technical: SAML metadata configurable per organization",
        "Technical: Errors in SAML flow handled gracefully with user feedback"
      ],
      "estimatedEffort": 24,
      "storyPoints": 8,
      "dependencies": [],
      "isSpike": false,
      "expectedOutcomes": [],
      "status": "approved",
      "llm_id": "us-021",
      "llmId": "us-021"
    },
    {
      "id": "0b71d701-32b4-4653-815a-141f65c0ab36",
      "title": "Implement Simple Login and Query Interface for Users",
      "description": "As a viewer or editor, I want to log in and query documents easily, so that I can find information quickly",
      "epic": "epic-core-user-workflow-onboarding",
      "epicId": "30f2d4cf-1d59-4659-9dba-41436f4e6470",
      "priority": "high",
      "acceptanceCriteria": [
        "Functional: Users can log in via SSO or local fallback",
        "Functional: Users see a simple search bar to enter queries",
        "Functional: Query results display answers with citations and links",
        "Technical: Frontend React components for login and search",
        "Technical: Backend supports authentication and query APIs"
      ],
      "estimatedEffort": 20,
      "storyPoints": 8,
      "dependencies": [
        "4bc93892-023b-460f-adc3-a7179c81b722",
        "f882cf33-6f83-48a9-b580-5fe62d87fa09"
      ],
      "isSpike": false,
      "expectedOutcomes": [],
      "status": "approved",
      "llm_id": "us-020",
      "llmId": "us-020"
    },
    {
      "id": "f13817a7-d052-435f-9af4-d18438923327",
      "title": "Implement User Creation and Assignment by Admin",
      "description": "As an admin, I want to create users and assign them to collections, so that team members can access relevant documents",
      "epic": "epic-core-user-workflow-onboarding",
      "epicId": "30f2d4cf-1d59-4659-9dba-41436f4e6470",
      "priority": "high",
      "acceptanceCriteria": [
        "Functional: Admin can create users and assign roles and collections",
        "Functional: Users receive invitation or notification to log in",
        "Technical: Backend APIs support user creation and assignment",
        "Technical: Frontend UI supports user management and assignment",
        "Technical: Permissions enforced on user assignments"
      ],
      "estimatedEffort": 20,
      "storyPoints": 8,
      "dependencies": [
        "42dd9560-1229-4fd2-b77c-0448d25409dd",
        "45f008df-44fb-4233-b644-e9858cd3b759",
        "e7aa8ab6-008f-4b8c-8ad4-570257d5ca06"
      ],
      "isSpike": false,
      "expectedOutcomes": [],
      "status": "approved",
      "llm_id": "us-019",
      "llmId": "us-019"
    },
    {
      "id": "6208c1c5-76b6-4e31-a61a-774d544c7904",
      "title": "Implement Admin Sign-Up and Workspace Creation Flow",
      "description": "As an admin, I want to sign up and create a workspace, so that I can start using the system",
      "epic": "epic-core-user-workflow-onboarding",
      "epicId": "30f2d4cf-1d59-4659-9dba-41436f4e6470",
      "priority": "high",
      "acceptanceCriteria": [
        "Functional: Admin can register and create workspace via frontend UI",
        "Functional: Workspace is created with default settings and initial collection",
        "Technical: Backend supports workspace creation APIs",
        "Technical: Frontend provides guided setup wizard",
        "Technical: User session established post sign-up"
      ],
      "estimatedEffort": 16,
      "storyPoints": 5,
      "dependencies": [
        "4bc93892-023b-460f-adc3-a7179c81b722",
        "45f008df-44fb-4233-b644-e9858cd3b759"
      ],
      "isSpike": false,
      "expectedOutcomes": [],
      "status": "approved",
      "llm_id": "us-018",
      "llmId": "us-018"
    },
    {
      "id": "9d9a1745-8f55-42e4-b237-0f5efd391741",
      "title": "Design and Implement REST API Endpoint for Natural Language Querying",
      "description": "As a viewer, I want to query documents via REST API, so that I can integrate search into other applications",
      "epic": "epic-core-api-first-design",
      "epicId": "3b7c566d-692f-4742-8a3a-06c35f512844",
      "priority": "high",
      "acceptanceCriteria": [
        "Functional: API accepts question and collection_id, returns answer with citations",
        "Functional: API enforces rate limiting and permissions",
        "Technical: API integrates with RAG pipeline components",
        "Technical: API returns consistent JSON schema for answers and citations",
        "Technical: API documented and versioned"
      ],
      "estimatedEffort": 16,
      "storyPoints": 5,
      "dependencies": [
        "f882cf33-6f83-48a9-b580-5fe62d87fa09",
        "a23bb700-bd6a-4d83-8229-e926c0733b23"
      ],
      "isSpike": false,
      "expectedOutcomes": [],
      "status": "approved",
      "llm_id": "us-017",
      "llmId": "us-017"
    },
    {
      "id": "62bd29d4-0f85-4ea8-b4f8-72745aab041d",
      "title": "Design and Implement REST API Endpoints for Document and Collection Management",
      "description": "As an editor or admin, I want to manage documents and collections via REST APIs, so that I can integrate with other tools",
      "epic": "epic-core-api-first-design",
      "epicId": "3b7c566d-692f-4742-8a3a-06c35f512844",
      "priority": "high",
      "acceptanceCriteria": [
        "Functional: API supports CRUD operations for collections and documents",
        "Functional: API supports file upload via multipart/form-data",
        "Technical: API endpoints enforce permissions and validate inputs",
        "Technical: API supports pagination and filtering where applicable",
        "Technical: API documented with OpenAPI and versioned"
      ],
      "estimatedEffort": 24,
      "storyPoints": 8,
      "dependencies": [
        "45f008df-44fb-4233-b644-e9858cd3b759",
        "e53e9568-7744-4ea0-b8bd-21f00bf99b30",
        "a23bb700-bd6a-4d83-8229-e926c0733b23"
      ],
      "isSpike": false,
      "expectedOutcomes": [],
      "status": "approved",
      "llm_id": "us-016",
      "llmId": "us-016"
    },
    {
      "id": "8492a709-2452-4f86-9abc-6e327ce60924",
      "title": "Design and Implement REST API Endpoints for User Management",
      "description": "As an admin, I want to manage users via REST APIs, so that I can automate user administration",
      "epic": "epic-core-api-first-design",
      "epicId": "3b7c566d-692f-4742-8a3a-06c35f512844",
      "priority": "high",
      "acceptanceCriteria": [
        "Functional: API supports listing, creating, updating, and deleting users",
        "Functional: API enforces role-based access control",
        "Technical: Endpoints documented with OpenAPI schema",
        "Technical: API versioning implemented under /api/v1/",
        "Technical: API returns standardized error codes and messages"
      ],
      "estimatedEffort": 20,
      "storyPoints": 8,
      "dependencies": [
        "42dd9560-1229-4fd2-b77c-0448d25409dd",
        "4bc93892-023b-460f-adc3-a7179c81b722"
      ],
      "isSpike": false,
      "expectedOutcomes": [],
      "status": "approved",
      "llm_id": "us-015",
      "llmId": "us-015"
    },
    {
      "id": "a89cc6b2-a780-4e27-8ab0-1e1cc1ac38e5",
      "title": "Implement Tenant-Aware API Endpoints",
      "description": "As the system, I want API endpoints to be tenant-aware, so that data returned and modified is scoped to the authenticated user's organization",
      "epic": "epic-core-multi-tenant-architecture",
      "epicId": "57a468cd-bb72-47cc-bb26-380e722c94ce",
      "priority": "medium",
      "acceptanceCriteria": [
        "Functional: API endpoints filter data by organization context",
        "Functional: Users cannot access data from other organizations",
        "Technical: TenantResolver middleware extracts organization from JWT claims",
        "Technical: Database queries include organization_id filters",
        "Technical: API returns 403 on cross-tenant access attempts"
      ],
      "estimatedEffort": 20,
      "storyPoints": 8,
      "dependencies": [
        "724755ec-81b0-4475-9b9d-3decf0309f03",
        "4bc93892-023b-460f-adc3-a7179c81b722"
      ],
      "isSpike": false,
      "expectedOutcomes": [],
      "status": "approved",
      "llm_id": "us-014",
      "llmId": "us-014"
    },
    {
      "id": "724755ec-81b0-4475-9b9d-3decf0309f03",
      "title": "Design Multi-Tenant Data Model in PostgreSQL",
      "description": "As the system architect, I want to design a multi-tenant data model that isolates organizations' data, so that multiple companies can securely use the platform",
      "epic": "epic-core-multi-tenant-architecture",
      "epicId": "57a468cd-bb72-47cc-bb26-380e722c94ce",
      "priority": "medium",
      "acceptanceCriteria": [
        "Functional: Data model supports organization isolation for users, collections, documents",
        "Technical: PostgreSQL schema includes organizations and organization_id foreign keys",
        "Technical: Data access queries are tenant-aware and filter by organization",
        "Technical: Migration scripts created to add multi-tenant support",
        "Technical: Model supports future tenant-aware API endpoints"
      ],
      "estimatedEffort": 16,
      "storyPoints": 5,
      "dependencies": [
        "42dd9560-1229-4fd2-b77c-0448d25409dd"
      ],
      "isSpike": false,
      "expectedOutcomes": [],
      "status": "approved",
      "llm_id": "us-013",
      "llmId": "us-013"
    },
    {
      "id": "4bc93892-023b-460f-adc3-a7179c81b722",
      "title": "Integrate SSO Authentication with Permissions",
      "description": "As the system, I want to integrate SAML/OIDC SSO authentication with user and permission management, so that enterprise users can securely log in",
      "epic": "epic-core-permissions-layer",
      "epicId": "f8082d2b-842e-4d99-8694-bff52e87c167",
      "priority": "high",
      "acceptanceCriteria": [
        "Functional: Users can authenticate via SAML and OIDC SSO providers",
        "Functional: SSO login creates or links user accounts with roles and collections",
        "Technical: Authentication middleware supports SAML and OIDC protocols",
        "Technical: JWT tokens issued post-authentication with user claims",
        "Technical: Session management and token validation implemented"
      ],
      "estimatedEffort": 24,
      "storyPoints": 8,
      "dependencies": [],
      "isSpike": false,
      "expectedOutcomes": [],
      "status": "approved",
      "llm_id": "us-012",
      "llmId": "us-012"
    },
    {
      "id": "a23bb700-bd6a-4d83-8229-e926c0733b23",
      "title": "Enforce Collection-Level Permissions in API",
      "description": "As the system, I want to enforce collection-level permissions on all document and query APIs, so that users only access authorized data",
      "epic": "epic-core-permissions-layer",
      "epicId": "f8082d2b-842e-4d99-8694-bff52e87c167",
      "priority": "high",
      "acceptanceCriteria": [
        "Functional: Users can only query documents in collections they are assigned to",
        "Functional: Upload and management APIs check user collection membership",
        "Technical: Permissions engine integrated into FastAPI middleware",
        "Technical: API returns 403 Forbidden for unauthorized access",
        "Technical: Permissions checks cover all relevant endpoints"
      ],
      "estimatedEffort": 20,
      "storyPoints": 8,
      "dependencies": [
        "42dd9560-1229-4fd2-b77c-0448d25409dd",
        "45f008df-44fb-4233-b644-e9858cd3b759",
        "e53e9568-7744-4ea0-b8bd-21f00bf99b30"
      ],
      "isSpike": false,
      "expectedOutcomes": [],
      "status": "approved",
      "llm_id": "us-011",
      "llmId": "us-011"
    },
    {
      "id": "42dd9560-1229-4fd2-b77c-0448d25409dd",
      "title": "Implement User Roles and Role Management",
      "description": "As an admin, I want to assign roles (admin, editor, viewer) to users, so that I can control their permissions",
      "epic": "epic-core-permissions-layer",
      "epicId": "f8082d2b-842e-4d99-8694-bff52e87c167",
      "priority": "high",
      "acceptanceCriteria": [
        "Functional: Admin can assign and change user roles",
        "Functional: Roles determine access rights in the system",
        "Technical: Roles and user_roles tables implemented in PostgreSQL",
        "Technical: API endpoints enforce role-based access control",
        "Technical: Frontend UI for role management"
      ],
      "estimatedEffort": 16,
      "storyPoints": 5,
      "dependencies": [
        "45f008df-44fb-4233-b644-e9858cd3b759"
      ],
      "isSpike": false,
      "expectedOutcomes": [],
      "status": "approved",
      "llm_id": "us-010",
      "llmId": "us-010"
    },
    {
      "id": "e7aa8ab6-008f-4b8c-8ad4-570257d5ca06",
      "title": "Allow Admins to Assign Users to Collections",
      "description": "As an admin, I want to assign users to document collections, so that I can control access to documents",
      "epic": "epic-core-document-upload-management",
      "epicId": "3155fb16-86ee-412a-8d0b-40c58978d9a1",
      "priority": "high",
      "acceptanceCriteria": [
        "Functional: Admin can assign and remove users from collections",
        "Functional: User collection assignments are enforced in permissions",
        "Technical: Assignments stored in user_collections table in PostgreSQL",
        "Technical: API endpoints for assignment enforce admin role",
        "Technical: Frontend UI for managing user assignments to collections"
      ],
      "estimatedEffort": 12,
      "storyPoints": 5,
      "dependencies": [
        "45f008df-44fb-4233-b644-e9858cd3b759",
        "42dd9560-1229-4fd2-b77c-0448d25409dd"
      ],
      "isSpike": false,
      "expectedOutcomes": [],
      "status": "approved",
      "llm_id": "us-009",
      "llmId": "us-009"
    },
    {
      "id": "e53e9568-7744-4ea0-b8bd-21f00bf99b30",
      "title": "Enable Editors to Upload and Manage Documents in Collections",
      "description": "As an editor, I want to upload documents into collections and manage them, so that I can maintain the knowledge base",
      "epic": "epic-core-document-upload-management",
      "epicId": "3155fb16-86ee-412a-8d0b-40c58978d9a1",
      "priority": "high",
      "acceptanceCriteria": [
        "Functional: Editors can upload documents to assigned collections",
        "Functional: Editors can view list of documents in collections",
        "Functional: Editors can delete documents they uploaded",
        "Technical: Upload API validates user role and collection membership",
        "Technical: Frontend document upload and management UI supports editors"
      ],
      "estimatedEffort": 20,
      "storyPoints": 8,
      "dependencies": [
        "45f008df-44fb-4233-b644-e9858cd3b759",
        "e4568bdb-c319-4ed5-8899-4c1d85757305"
      ],
      "isSpike": false,
      "expectedOutcomes": [],
      "status": "approved",
      "llm_id": "us-008",
      "llmId": "us-008"
    },
    {
      "id": "45f008df-44fb-4233-b644-e9858cd3b759",
      "title": "Implement Document Collections CRUD",
      "description": "As an admin, I want to create, read, update, and delete document collections, so that I can organize documents logically",
      "epic": "epic-core-document-upload-management",
      "epicId": "3155fb16-86ee-412a-8d0b-40c58978d9a1",
      "priority": "high",
      "acceptanceCriteria": [
        "Functional: Admin can create new collections with name and description",
        "Functional: Collections can be listed, updated, and deleted via API and frontend",
        "Technical: Collections stored in PostgreSQL with proper indexing",
        "Technical: API endpoints enforce admin/editor roles for collection management",
        "Technical: Frontend collection management UI implemented in React"
      ],
      "estimatedEffort": 16,
      "storyPoints": 5,
      "dependencies": [
        "e4568bdb-c319-4ed5-8899-4c1d85757305"
      ],
      "isSpike": false,
      "expectedOutcomes": [],
      "status": "approved",
      "llm_id": "us-007",
      "llmId": "us-007"
    },
    {
      "id": "b4a74558-170a-4610-8b22-0c51fefee1fa",
      "title": "Integrate Self-Hosted LLM Inference Using Ollama",
      "description": "As the system, I want to perform all LLM inference locally using Ollama, so that no data leaves the customer's infrastructure",
      "epic": "epic-core-rag-pipeline",
      "epicId": "d00e5ae6-b1a2-4202-9dea-fc55127c51c2",
      "priority": "high",
      "acceptanceCriteria": [
        "Functional: LLM inference requests are routed to local Ollama service",
        "Functional: No external API calls to third-party LLM providers occur",
        "Technical: Ollama is deployed as a Docker container and accessible via REST API",
        "Technical: Backend handles LLM prompt construction and response parsing",
        "Technical: LLM inference latency meets performance targets"
      ],
      "estimatedEffort": 16,
      "storyPoints": 5,
      "dependencies": [
        "f882cf33-6f83-48a9-b580-5fe62d87fa09"
      ],
      "isSpike": false,
      "expectedOutcomes": [],
      "status": "approved",
      "llm_id": "us-006",
      "llmId": "us-006"
    },
    {
      "id": "dae85381-58ba-45d8-a553-64209a750f2f",
      "title": "Implement Single-Turn Q&A Without Chat History",
      "description": "As a viewer, I want to perform single-turn queries without chat history, so that I can get immediate answers without session context",
      "epic": "epic-core-rag-pipeline",
      "epicId": "d00e5ae6-b1a2-4202-9dea-fc55127c51c2",
      "priority": "high",
      "acceptanceCriteria": [
        "Functional: Each query is independent with no stored conversation context",
        "Functional: System does not store or use previous queries for answer generation",
        "Technical: Backend query endpoint resets context per request",
        "Technical: No chat history data structures are maintained",
        "Technical: Frontend UI does not display or store chat history"
      ],
      "estimatedEffort": 8,
      "storyPoints": 3,
      "dependencies": [
        "f882cf33-6f83-48a9-b580-5fe62d87fa09"
      ],
      "isSpike": false,
      "expectedOutcomes": [],
      "status": "approved",
      "llm_id": "us-005",
      "llmId": "us-005"
    },
    {
      "id": "f882cf33-6f83-48a9-b580-5fe62d87fa09",
      "title": "Implement Natural Language Querying with RAG Pipeline",
      "description": "As a viewer, I want to enter natural language queries and receive plain English answers with source citations, so that I can quickly find relevant information",
      "epic": "epic-core-rag-pipeline",
      "epicId": "d00e5ae6-b1a2-4202-9dea-fc55127c51c2",
      "priority": "high",
      "acceptanceCriteria": [
        "Functional: User can submit a query via API and frontend search bar",
        "Functional: System returns an answer generated by local LLM with 2-3 source citations",
        "Functional: Citations link to original document chunks with snippet and page info",
        "Technical: Query handler retrieves top-k chunks from Qdrant based on embedding similarity",
        "Technical: LLM inference is performed locally using Ollama with prompt constructed from retrieved chunks"
      ],
      "estimatedEffort": 24,
      "storyPoints": 8,
      "dependencies": [
        "fbf00704-6f6c-466e-bf5a-1119edb5c9ba"
      ],
      "isSpike": false,
      "expectedOutcomes": [],
      "status": "approved",
      "llm_id": "us-004",
      "llmId": "us-004"
    },
    {
      "id": "fbf00704-6f6c-466e-bf5a-1119edb5c9ba",
      "title": "Generate Embeddings for Document Chunks and Store in Qdrant",
      "description": "As the system, I want to generate vector embeddings for document chunks and store them in Qdrant, so that semantic search queries can retrieve relevant chunks",
      "epic": "epic-core-rag-pipeline",
      "epicId": "d00e5ae6-b1a2-4202-9dea-fc55127c51c2",
      "priority": "high",
      "acceptanceCriteria": [
        "Functional: Embeddings are generated for all parsed chunks using local embedding model",
        "Functional: Embeddings are stored in Qdrant with metadata linking to document and chunk",
        "Technical: Embedding generation is batched and asynchronous",
        "Technical: Qdrant collections are created and indexed appropriately",
        "Technical: Embedding failures are logged and retried"
      ],
      "estimatedEffort": 20,
      "storyPoints": 8,
      "dependencies": [
        "87772124-3bce-4461-be87-8a0c4b2ed6a8"
      ],
      "isSpike": false,
      "expectedOutcomes": [],
      "status": "approved",
      "llm_id": "us-003",
      "llmId": "us-003"
    },
    {
      "id": "87772124-3bce-4461-be87-8a0c4b2ed6a8",
      "title": "Implement Document Parsing and Chunking for PDF and DOCX",
      "description": "As the system, I want to parse uploaded PDF and DOCX files into text chunks, so that they can be indexed for semantic search",
      "epic": "epic-core-rag-pipeline",
      "epicId": "d00e5ae6-b1a2-4202-9dea-fc55127c51c2",
      "priority": "high",
      "acceptanceCriteria": [
        "Functional: Uploaded documents are parsed into logical text chunks",
        "Functional: Each chunk is stored with metadata including document ID and chunk index",
        "Technical: Parsing supports page ranges and preserves text order",
        "Technical: Chunk data is stored in PostgreSQL document_chunks table",
        "Technical: Parsing process is asynchronous and reports status"
      ],
      "estimatedEffort": 20,
      "storyPoints": 8,
      "dependencies": [
        "e4568bdb-c319-4ed5-8899-4c1d85757305"
      ],
      "isSpike": false,
      "expectedOutcomes": [],
      "status": "approved",
      "llm_id": "us-002",
      "llmId": "us-002"
    },
    {
      "id": "e4568bdb-c319-4ed5-8899-4c1d85757305",
      "title": "Implement Document Upload Support for PDF and DOCX",
      "description": "As an editor, I want to upload PDF and DOCX documents, so that I can add knowledge sources to the system",
      "epic": "epic-core-rag-pipeline",
      "epicId": "d00e5ae6-b1a2-4202-9dea-fc55127c51c2",
      "priority": "high",
      "acceptanceCriteria": [
        "Functional: Editor can upload PDF and DOCX files via API and frontend",
        "Functional: Uploaded files are stored securely in file storage",
        "Technical: Backend validates file type and size before accepting upload",
        "Technical: Files are saved with unique identifiers and metadata stored in PostgreSQL",
        "Technical: Upload endpoint returns success status and document metadata"
      ],
      "estimatedEffort": 16,
      "storyPoints": 5,
      "dependencies": [],
      "isSpike": false,
      "expectedOutcomes": [],
      "status": "approved",
      "llm_id": "us-001",
      "llmId": "us-001"
    }
  ],
  "count": 52,
  "spikeStoriesCount": 9,
  "regularStoriesCount": 43
}