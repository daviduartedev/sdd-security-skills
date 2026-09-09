# ASVS 5.0.0 applicability mapping

Shared once for this collection. Answers **when is this area relevant?** for a change. It does not reproduce OWASP ASVS requirement bodies.

When a specific requirement is named, use the versioned form `v5.0.0-X.X.X` (example: `v5.0.0-8.2.1`). Load only the areas that apply.

Each area notes a **design** lens (threats and invariants) and an **implementation** lens (what to look for in a diff).

## V1 Encoding and Sanitization

Relevant when untrusted data is decoded, encoded, escaped, sanitized, deserialized, or handed to an interpreter (HTML, SQL, OS, LDAP, templates, XML, and similar).

- Design: trust boundaries where data changes context; injection and unsafe-deserialization surfaces.
- Implementation: encoding at the interpreter edge, parameterized queries, sanitizer use, parser configuration.
- Example IDs: `v5.0.0-1.2.4`, `v5.0.0-1.3.1`, `v5.0.0-1.5.1`.

## V2 Validation and Business Logic

Relevant when the change accepts input, enforces domain rules, sequences a workflow, or exposes a costly or abuseable operation.

- Design: expected shape of data, step order, quotas, and who can drive the flow.
- Implementation: server-side validation, skipped steps, missing limits, missing anti-automation on expensive actions.
- Example IDs: `v5.0.0-2.2.1`, `v5.0.0-2.3.1`, `v5.0.0-2.4.1`.

## V3 Web Frontend Security

Relevant when the change ships browser-facing HTML, JavaScript, cookies, or HTTP security headers.

- Design: what the browser is trusted to enforce; cookie purpose; third-party script surface.
- Implementation: XSS sinks, cookie flags, CSP/HSTS and related headers, origin isolation, resource integrity.
- Example IDs: `v5.0.0-3.2.1`, `v5.0.0-3.3.1`, `v5.0.0-3.4.1`.
- Skip when the diff is backend-only with no browser surface.

## V4 API and Web Service

Relevant when HTTP APIs, GraphQL, or WebSockets are added or changed.

- Design: message contracts, authentication to the API, GraphQL exposure, socket authorization.
- Implementation: request parsing, mass assignment, GraphQL depth/allowlisting, WebSocket authz on each message.
- Example IDs: `v5.0.0-4.1.1`, `v5.0.0-4.3.1`, `v5.0.0-4.4.1`.

## V5 File Handling

Relevant when the change uploads, stores, transforms, or serves files.

- Design: who may upload; allowed types; where files land; how they are served.
- Implementation: name/path traversal, content-type vs content, executable upload, unsafe serving of user files.
- Example IDs: `v5.0.0-5.2.1`, `v5.0.0-5.3.1`, `v5.0.0-5.4.1`.

## V6 Authentication

Relevant when sign-in, passwords, MFA, recovery, or an identity provider is added or changed.

- Design: authenticator strength, recovery paths, lockout vs stuffing, IdP trust.
- Implementation: credential handling, MFA bypass, recovery tokens, IdP callback/state validation.
- Example IDs: `v5.0.0-6.2.1`, `v5.0.0-6.3.1`, `v5.0.0-6.5.1`.

## V7 Session Management

Relevant when server-side sessions, session cookies, timeout, logout, or session fixation defenses change.

- Design: session lifetime, binding, logout completeness, fixation/reuse.
- Implementation: token issuance, rotation, timeout, invalidation, concurrent session rules.
- Example IDs: `v5.0.0-7.2.1`, `v5.0.0-7.3.1`, `v5.0.0-7.4.1`.
- Prefer V9 when the change is self-contained tokens rather than a server session.

## V8 Authorization

Relevant when who may perform an operation, read a record, or cross a tenant/privilege boundary changes, including IDOR-style object access.

- Design: actors, roles, tenancy, privilege boundaries, denied-by-default.
- Implementation: missing checks on object IDs, horizontal/vertical privilege gaps, function-level bypass.
- Example IDs: `v5.0.0-8.2.1`, `v5.0.0-8.3.1`.

## V9 Self-contained Tokens

Relevant when JWTs or other self-contained tokens are issued, parsed, or used for authn/authz.

- Design: issuer, audience, lifetime, claims that actually authorize, revocation story.
- Implementation: algorithm confusion, missing signature verify, weak secrets, sensitive data in claims.
- Example IDs: `v5.0.0-9.1.1`, `v5.0.0-9.2.1`.

## V10 OAuth and OIDC

Relevant when the change is an OAuth/OIDC client, resource server, authorization server, or consent flow.

- Design: roles in the protocol, redirect URIs, grant types, consent.
- Implementation: `state`/`nonce`, PKCE, token storage, confused-deputy, redirect URI allowlisting.
- Example IDs: `v5.0.0-10.1.1`, `v5.0.0-10.2.1`.
- Skip protocol-provider sections when the app is only a client.

## V11 Cryptography

Relevant when the change chooses algorithms, keys, randomness, hashing, or encrypts data at rest or in use.

- Design: what must be confidential or integrity-protected; key ownership.
- Implementation: home-grown crypto, ECB, weak hashes for passwords, reuse of nonces, insecure randomness.
- Example IDs: `v5.0.0-11.2.1`, `v5.0.0-11.3.1`, `v5.0.0-11.5.1`.

## V12 Secure Communication

Relevant when TLS, HTTPS, or service-to-service transport is configured or bypassed.

- Design: what must be in transit protection; certificate trust.
- Implementation: TLS disabled, weak ciphers, hostname verification skipped, cleartext credentials.
- Example IDs: `v5.0.0-12.1.1`, `v5.0.0-12.2.1`.

## V13 Configuration

Relevant when environment config, backend URLs, secret storage, or debug/error leakage changes.

- Design: where secrets live; what is unsafe to expose; environment separation.
- Implementation: secrets in repo or images, verbose debug in production, unsafe default config.
- Example IDs: `v5.0.0-13.3.1`, `v5.0.0-13.4.1`.

## V14 Data Protection

Relevant when sensitive data is stored, displayed, exported, cached, or sent to the client.

- Design: classification, retention, which fields the client actually needs.
- Implementation: extra fields in API responses, secrets in logs/local storage, missing encryption at rest where required.
- Example IDs: `v5.0.0-14.2.1`, `v5.0.0-14.3.1`.

## V15 Secure Coding and Architecture

Relevant when architecture, dependency trust, defensive coding, or concurrency/isolation of security-sensitive operations changes.

- Design: trust of dependencies, isolation of privileged components, documented security architecture.
- Implementation: unsafe APIs, race conditions on security checks, supply-chain/config of dependencies that execute code.
- Example IDs: `v5.0.0-15.2.1`, `v5.0.0-15.3.1`.

## V16 Security Logging and Error Handling

Relevant when authentication, authorization, or other security-relevant events are logged, or when error paths change.

- Design: which events must be auditable; what must never appear in logs or user-visible errors.
- Implementation: missing security events, stack traces to clients, secrets in log lines, log injection.
- Example IDs: `v5.0.0-16.3.1`, `v5.0.0-16.5.1`.

## V17 WebRTC

Relevant when the change uses WebRTC, TURN, media, or signaling.

- Design: who may join; TURN authentication; media confidentiality.
- Implementation: unauthenticated TURN, signaling spoofing, media sent to the wrong peer.
- Example IDs: `v5.0.0-17.1.1`, `v5.0.0-17.3.1`.
- Skip for ordinary HTTP/REST or typical SaaS API changes with no real-time media.
