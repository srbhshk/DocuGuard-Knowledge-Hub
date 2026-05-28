{
  "metadata": {
    "ideaId": "4ecf9daf-5a1a-4b54-a4eb-990febdc28a9",
    "source": "idea_and_qa",
    "projectId": "6ed935c4-df4d-49ef-a9de-5cd1c25f46c2",
    "extractedAt": "2026-05-11T12:37:50.510Z",
    "totalFeatures": 13
  },
  "nfrFeatures": [
    {
      "id": "nfr-1",
      "name": "Data Security and Access Control",
      "category": "nfr",
      "priority": "high",
      "userImpact": "Protects enterprise data confidentiality and compliance with security policies.",
      "description": "Ensure robust security to protect sensitive enterprise data with enforced permissions and secure authentication.",
      "integrations": [
        "SAML",
        "OIDC"
      ],
      "requirements": [
        "Enforce collection-level permissions in v1",
        "Integrate with enterprise SSO for authentication",
        "Plan for document-level permissions in v2"
      ],
      "technicalRequirements": [
        "Secure API authorization checks",
        "Encrypted data storage and transmission"
      ]
    },
    {
      "id": "nfr-2",
      "name": "Performance and Latency Targets",
      "category": "nfr",
      "priority": "high",
      "userImpact": "Provides users with quick answers, improving usability and satisfaction.",
      "description": "Maintain query response latency under 3 seconds to ensure a smooth user experience.",
      "integrations": [],
      "requirements": [
        "Optimize RAG pipeline and vector search",
        "Efficient LLM inference locally"
      ],
      "technicalRequirements": [
        "Low-latency vector search with Qdrant",
        "Fast LLM inference with Ollama",
        "Backend performance tuning"
      ]
    },
    {
      "id": "nfr-3",
      "name": "Open-Source Component Usage",
      "category": "nfr",
      "priority": "high",
      "userImpact": "Gives customers confidence in transparency and control over the system.",
      "description": "Preference for open-source components to avoid vendor lock-in and increase transparency.",
      "integrations": [],
      "requirements": [
        "Use open-source backend and frontend frameworks",
        "Avoid proprietary or opinionated libraries like LangChain"
      ],
      "technicalRequirements": [
        "Python, FastAPI, React, Qdrant, Ollama",
        "Custom RAG pipeline implementation"
      ]
    }
  ],
  "coreFeatures": [
    {
      "id": "feature-1",
      "name": "Retrieval-Augmented Generation (RAG) Pipeline",
      "category": "core",
      "priority": "high",
      "userImpact": "Allows users to easily find relevant information from uploaded documents through natural language queries, improving knowledge access and productivity.",
      "description": "Core functionality enabling users to upload documents and query them using natural language, leveraging a RAG model to provide answers with source citations.",
      "integrations": [],
      "requirements": [
        "Support document upload for PDF and DOCX in v1, with TXT support planned post-launch",
        "Enable natural language querying with plain English answers",
        "Return 2-3 source citations per answer linking to document and section",
        "No chat history in v1, single-turn Q&A only",
        "Self-hosted LLM inference from day one"
      ],
      "technicalRequirements": [
        "Custom RAG pipeline implementation without LangChain",
        "Integration with vector storage (Qdrant)",
        "Local LLM inference using Ollama",
        "Python backend with FastAPI",
        "Frontend with React"
      ]
    },
    {
      "id": "feature-2",
      "name": "Document Upload and Management",
      "category": "core",
      "priority": "high",
      "userImpact": "Enables teams to centralize and structure their knowledge base for efficient querying.",
      "description": "Functionality for admins and editors to upload and organize documents into collections for querying.",
      "integrations": [],
      "requirements": [
        "Support PDF and DOCX file formats for upload in v1",
        "Allow organizing documents into collections",
        "Editors can upload and manage documents",
        "Admins assign users to collections"
      ],
      "technicalRequirements": [
        "File upload handling in backend",
        "Storage and metadata management in PostgreSQL",
        "Vector indexing in Qdrant"
      ]
    },
    {
      "id": "feature-3",
      "name": "Basic Permissions Layer",
      "category": "core",
      "priority": "high",
      "userImpact": "Ensures users only access authorized documents, maintaining data security and compliance.",
      "description": "Simple permissions system where an admin assigns users to document collections, controlling access at the collection level.",
      "integrations": [],
      "requirements": [
        "Three user roles: admin (full access), editor (upload/manage docs), viewer (query only)",
        "Admins create users and assign them to collections",
        "Permissions enforced on document collections",
        "Document-level permissions deferred to v2"
      ],
      "technicalRequirements": [
        "User and role management in PostgreSQL",
        "Access control enforcement in API",
        "Authentication integration with SSO (SAML/OIDC)"
      ]
    },
    {
      "id": "feature-4",
      "name": "Multi-Tenant Architecture (Deferred)",
      "category": "core",
      "priority": "medium",
      "userImpact": "Allows the product to serve multiple companies securely and independently.",
      "description": "Support for multiple organizations with isolated workspaces and data, planned for post-v1.",
      "integrations": [],
      "requirements": [
        "Isolated data and permissions per tenant",
        "Separate admin and user management per organization"
      ],
      "technicalRequirements": [
        "Multi-tenant data model design in PostgreSQL",
        "Tenant-aware API endpoints"
      ]
    },
    {
      "id": "feature-5",
      "name": "API-First Design",
      "category": "core",
      "priority": "high",
      "userImpact": "Enables automation, integration with other tools, and flexible client implementations.",
      "description": "Expose all core functionalities via APIs to enable integration and extensibility beyond chatbot UI.",
      "integrations": [],
      "requirements": [
        "Document upload, querying, user and permission management exposed via REST APIs",
        "API documentation and versioning"
      ],
      "technicalRequirements": [
        "FastAPI backend with well-designed REST endpoints",
        "Authentication and authorization on APIs"
      ]
    },
    {
      "id": "feature-6",
      "name": "User Workflow and Onboarding",
      "category": "core",
      "priority": "high",
      "userImpact": "Reduces friction for teams to start using the system quickly.",
      "description": "Smooth first-use experience where admin creates workspace, uploads documents, assigns users, and users query documents.",
      "integrations": [],
      "requirements": [
        "Admin sign-up and workspace creation",
        "Document upload into collections",
        "User creation and assignment to collections by admin",
        "Simple login and query interface for users"
      ],
      "technicalRequirements": [
        "Frontend React implementation for admin and user flows",
        "Backend support for user and workspace lifecycle"
      ]
    }
  ],
  "otherFeatures": [],
  "integrationFeatures": [
    {
      "id": "integration-1",
      "name": "SSO Integration (SAML/OIDC)",
      "category": "integration",
      "priority": "high",
      "userImpact": "Facilitates secure and seamless user login aligned with enterprise policies.",
      "description": "Support single sign-on via SAML or OIDC protocols to enable enterprise authentication.",
      "integrations": [
        "SAML",
        "OIDC"
      ],
      "requirements": [
        "Implement SAML and OIDC authentication flows",
        "Allow configuration per organization",
        "Integrate with user and permission management"
      ],
      "technicalRequirements": [
        "Authentication middleware supporting SAML and OIDC",
        "Secure token handling and session management"
      ]
    },
    {
      "id": "integration-2",
      "name": "File Upload Support",
      "category": "integration",
      "priority": "high",
      "userImpact": "Allows users to bring in documents from various sources for querying.",
      "description": "Support uploading files in PDF, DOCX, and TXT formats initially, with connectors to external document sources planned post-launch.",
      "integrations": [
        "Confluence",
        "Notion",
        "Google Drive",
        "SharePoint"
      ],
      "requirements": [
        "Support PDF, DOCX, and TXT file uploads at launch",
        "Post-launch connectors for Confluence, Notion, Google Drive, SharePoint"
      ],
      "technicalRequirements": [
        "File parsing and indexing pipelines",
        "API connectors for external services"
      ]
    }
  ],
  "infrastructureFeatures": [
    {
      "id": "infra-1",
      "name": "Self-Hosted Deployment via Docker Compose",
      "category": "infrastructure",
      "priority": "high",
      "userImpact": "Enables customers to keep data on-premise, meeting security and compliance needs.",
      "description": "Deployment model where customers download and run the system on their own infrastructure using Docker Compose.",
      "integrations": [],
      "requirements": [
        "Provide Docker Compose configuration for all components",
        "Support local deployment of backend, frontend, vector store, and LLM inference",
        "Documentation for installation and operation"
      ],
      "technicalRequirements": [
        "Containerization of backend, frontend, Qdrant, Ollama LLM",
        "Networking and service orchestration in Docker Compose"
      ]
    },
    {
      "id": "infra-2",
      "name": "Scalability for Growing Organizations",
      "category": "infrastructure",
      "priority": "medium",
      "userImpact": "Ensures responsive and reliable service as user base and data grow.",
      "description": "Design infrastructure to handle growth from 1-3 organizations at launch to 15-20 organizations with increased users and documents within the first year.",
      "integrations": [],
      "requirements": [
        "Support up to 200 users and 50,000 documents per organization",
        "Handle 100-500 queries per day per organization",
        "Maintain query latency under 3 seconds"
      ],
      "technicalRequirements": [
        "Efficient vector search with Qdrant",
        "Optimized LLM inference performance",
        "Database indexing and query optimization"
      ]
    }
  ]
}