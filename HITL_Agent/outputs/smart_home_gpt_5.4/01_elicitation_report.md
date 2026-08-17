# 01 Elicitation Report — DigitalHome (DH) Smart Home Prototype

## 1. Original Requirements Text

```markdown
# DigitalHome Requirements Specification

This document specifies the requirements for the development of a "Smart House", called DigitalHome (DH), by the DigitalHomeOwner Division of HomeOwner Inc. A "Smart House" is a home management system that allows home residents to easily manage their daily lives by providing for a lifestyle that brings together security, environmental and energy management (temperature, humidity and lighting), entertainment, and communications. The Smart House components consist of household devices (e.g., a heating and air conditioning unit, a security system, and small appliances and lighting units, etc.), sensors and controllers for the devices, communication links between the components, and a computer system, which will manage the components. The DigitalHome Software Requirements Specification (SRS) is based on the DigitalHome Customer Need Statement. It is made up of a list of the principal features of the system. This initial version of DigitalHome will be a limited prototype version, which will be used by HomeOwner management to make business decisions about the future commercial development of DigitalHomeOwner products and services. Hence, the SRS is not intended as a comprehensive or complete specification of DigitalHome requirements. There is a supplementary document that provides additional detail and information about the DigitalHome requirements: the Digital Home Use Case Model [HO2010]. These document were prepared by the DigitalHomeOwner Division, in consultation with the Marketing Division of HomeOwner Inc.

The Digital Home system, for the purposes of this document, is a system that will allow a home user to manage devices that control the environment of a home. The user communicates through a personal web page on the DigitalHome web server or on a local home server. The DH web server communicates, through a home wireless gateway device, with the sensor and controller devices in the home. The product is based on the Digital Home High Level Requirements Definition [HLRD 2010] is intended as a prototype, which will allow business decisions to be made about future development of a commercial product. The scope of the project will be limited to the management of devices which control temperature, humidity, security, and power to small appliances and lighting units, through the use of a web-ready device. The prototype DH software system will be situated in a simulated environment. There will be no actual physical home and all sensors and controllers will be simulated.

---

### 3.2 Users Description

#### 3.2.1 DigitalHome Users
* **3.2.1.1** The general user shall be able to use the DH system capabilities to monitor and control the environment in his/her home.
* **3.2.1.3** Although the general user is not familiar with the technical features of the DH system, he/she is familiar with the use of a web interface and can perform simple web operations (logging in and logging out, browsing web pages, and submitting information and requests via a web interface).
* **3.2.1.4** A Master user will be designated, who shall be able to change the configuration of the system. For example, a Master User shall be able to add a user account or change the default parameter settings. He/she will have the same right as the DH Technician, described in section 3.2.2.4.

#### 3.2.2 DigitalHome Technician
* **3.2.2.1** A DH Technician is responsible for setting up and maintaining the configuration of a DH system.
* **3.2.2.2** A DH Technician has experience with the type of hardware, software, and web services associated with a system like the DH system.
* **3.2.2.3** A DH Technician is specially trained by DigitalHomeOwner to be familiar with the functionality, architecture, and operation of the DH system product.
* **3.2.2.4** A DH Technician will have rights beyond the DH General User, capable of setting up and making changes in the configuration of the system (e.g., setting system parameters and establishing user accounts), and starting and stopping operation of the DH System.

### 3.3 Development Constraints

* **3.3.1** The "prototype" version of the DigitalHome System (as specified in this document) must be completed within twelve months of inception.
* **3.3.2** The development team will consist of five engineers. The DigitalHomeOwner Director will provide management and communication support.
* **3.3.3** The development team will use the development process specified by the Digital HomeOwner Inc.
* **3.3.4** Where possible, the DigitalHome project will employ widely used, accepted, and available hardware and software technology and standards, both for product elements and for development tools. See section 3.4 for additional detail.
* **3.3.5** Because of potential market competition for DigitalHome products, the cost of DigitalHome elements (sensors, controllers, server, tools, etc.), for this project should be minimized. As part of the final project report the development team will describe their efforts to minimize costs, including price comparisons between DH elements and comparable/competitive elements.
* **3.3.6** The DH system will be tested in a simulated environment. There will be no actual physical home and all sensors and controllers will be simulated. However, the simulated environment will be realistic and adhere to the physical properties and constraints of an actual home and to real sensors and controllers.
* **3.3.7** Major changes to this document (e.g., changes in requirements) must be approved by the Director of the DigitalHome Owner Division.

### 3.4 Operational Environment

Although the system to be developed is a "proof of concept" system intended to help Homeowner Inc. to make marketing and development decisions, the following sections describe operational environment concerns and constraints; some of them are related to issues of long-term production and marketing of a DigitalHome product.

* **3.4.1** The home system shall require an Internet Service Provider (ISP). The ISP should be widely available (cable modem, high speed DSL), such as Bright House or Bellsouth FastAccess.

#### 3.4.2 DH Home Web Server
* **3.4.2.1** A DH System shall have the capability to establish an individual home web server hosted on a home computer. This server will provide:
  * **a.** Interaction with and control of the DH elements
  * **b.** Storage of DH plans and data.
  * **c.** Ability to establish and maintain DH User Accounts
  * **d.** Provide backup service for user account information, user plans and a home database

#### 3.4.3 Home DH Gateway Device
* **3.4.3.1** The DH Gateway device shall provide communication with all the DigitalHome devices and shall connect with a broadband Internet connection.
* **3.4.3.2** The Gateway shall contain an RF Module, which shall send and receive wireless communications between the Gateway and the other DigitalHome devices (sensors and controllers).
* **3.4.3.3** The Gateway device shall operate up to a 1000-foot range for indoor transmission.

#### 3.4.4 Sensors and Controllers
* **3.4.4.1** The system shall include digital programmable thermostats, which shall be used to monitor and regulate the temperature of an enclosed space.
  * **a.** The thermostat shall provide a reading of the current temperature in the space where the thermostat is located.
  * **b.** The controller part of thermostat shall provides a "set point" temperature that is used to control the flow of heat energy (by switching heating or cooling devices on or off as needed) to achieve the set point temperature.
  * **c.** The sensor part of the thermostat has a sensitivity range between 14°F and 104°F (-10°C and 40°C).
* **3.4.4.2** The system shall include digital programmable humidistats, which shall be used to monitor and regulate the humidity of an enclosed space.
  * **a.** The humidistat shall provide a reading of the current humidity in the space where the humidistat is located.
  * **b.** The humidistat shall provide a "set point" humidity that is used to control humidifiers and dehumidifiers achieve the set point humidity.
* **3.4.4.3** The system shall include magnetic alarm contact switches which shall be used to monitor entry through a door or window when the switch is active.
* **3.4.4.4** The system shall include security sound and light alarms, which can be activated when DigitalHome senses a security breach from a magnetic contact.
* **3.4.4.5** The system shall include digital programmable power switches which shall be used to monitor the current state of an appliance (e.g., a coffee maker is off or on).
* **3.4.4.6** The system shall be able to use a power switch to change the state of the appliance (e.g., from "off" to "on").
```

## 2. Stakeholder Q&A History

### Q1
**Question:** For this prototype, which user roles must be supported in the web interface, and what high-level permissions distinguish General User, Master User, and DH Technician?  
**Why asked:** The document names three roles and says Master User has the same rights as the technician, but the actual role boundaries are ambiguous. This is a core access-control rule that affects scope, security, and administration features.  
**Stakeholder answer:** the same as mentioned in the document

### Q2
**Question:** For the prototype’s planning and reporting scope, which of these capabilities are required: monthly planner, daily presets/schedules, and historical reports such as averages, min/max, and downtime logs?  
**Why asked:** The source mentions storage of plans and data but does not define whether planning/reporting features are actually in scope. This is a critical high-level business scope decision affecting several core modules.  
**Stakeholder answer:** all three

### Q3
**Question:** What authentication and security baseline is required for the prototype web access and backups—for example, username/password only, role-based access control, and whether TLS encryption is mandatory?  
**Why asked:** The document requires user accounts, backups, and Internet access but does not define the minimum authentication and transport security expectations. This is a critical non-functional and security requirement.  
**Stakeholder answer:** username password

## 3. Gap Analysis and Critical Ambiguities

This section documents the principal requirement gaps identified during the audit. Only the most critical items were escalated to the stakeholder; remaining items are recorded as assumptions or unresolved constraints to be handled carefully during downstream specification work.

### 3.1 User Roles and Access Control
- **Partially clarified.** The source defines three user types: General User, Master User, and DH Technician.
- **Confirmed by stakeholder:** the prototype should use the role definitions already stated in the source document.
- **Residual ambiguity:** the source still does not fully enumerate permission matrices by function. For example, it implies General Users can monitor/control the home environment, and Master User/DH Technician can configure the system, maintain accounts, set parameters, and start/stop the system.
- **Impact:** authentication, authorization, admin UI scope, auditability, and test scenarios.

### 3.2 Planning and Reporting Scope
- **Clarified by stakeholder:** the prototype must include:
  - monthly planner
  - daily presets/schedules
  - historical reports including averages, min/max, and downtime logs
- **Residual ambiguity:** no detailed report dimensions, retention windows, export formats, or filtering requirements are defined.
- **Impact:** storage model, reporting UI, simulation data generation, and acceptance criteria.

### 3.3 Authentication and Security Baseline
- **Clarified by stakeholder:** username/password authentication is required.
- **Critical unresolved scope gap:** stakeholder did not confirm role-based access control explicitly in the answer, but the source document itself implies role distinctions. Therefore RBAC remains inferable from the original source, not directly from the answer.
- **Unspecified:** TLS/HTTPS requirement, password policy, account lockout, password reset, backup encryption, session timeout, and audit logging.
- **Impact:** security posture of the prototype and compliance expectations.

### 3.4 Environmental Control Requirements
#### Thermostats
- The source specifies a sensing range of **14°F to 104°F (-10°C to 40°C)**.
- **Missing:**
  - set-point allowable range
  - set-point increment/granularity
  - number of schedule periods per day
  - default operating mode behavior when heating/cooling are both available
  - tolerance/deadband around set point
  - manual override behavior and duration
  - HVAC compatibility assumptions beyond generic heating/cooling switching
- **Impact:** control logic definition and planner behavior.

#### Humidistats
- The source states current humidity reading and humidity set point are supported.
- **Missing:**
  - humidity sensor operating range
  - set-point allowable range
  - increment/granularity
  - tolerance/deadband around humidity target
  - manual override behavior and duration
  - compatibility assumptions for humidifier/dehumidifier control
- **Impact:** incomplete control behavior and validation criteria.

### 3.5 Security and Safety Requirements
- Contact switches on doors/windows are in scope.
- Sound/light alarms are in scope and may activate on breach from a magnetic contact.
- **Missing:**
  - what constitutes a breach state (e.g., any active sensor open event)
  - armed/disarmed modes
  - entry/exit delays
  - whether alarms are silent, audible, visible, or combined by default
  - acknowledgement/reset rules after alarm activation
  - fail-safe behavior for gateway/server/sensor communication loss
- **Impact:** core security workflow remains underspecified.

### 3.6 Appliance and Power Management
- Power switches can monitor current state and change appliance state on/off.
- **Missing:**
  - supported appliance categories versus generic “small appliances and lighting units”
  - electrical constraints such as max voltage/current/load
  - default reset behavior after restart or communication failure
  - whether state changes may be scheduled through planner/presets
- **Impact:** safety limits and appliance control boundaries are vague.

### 3.7 Non-Functional and Quality-of-Service Constraints
- The source provides almost no measurable QoS targets.
- **Missing:**
  - UI refresh rate expectations
  - sensor sample/update rates
  - end-to-end command latency expectations
  - RF performance assumptions beyond “1000-foot indoor range”
  - reliability/failure-rate or MTBF targets
  - backup frequency, recovery point objective, and restore procedure
  - maximum number of users/devices supported in prototype
- **Impact:** acceptance testing and architecture tradeoffs are difficult to evaluate objectively.

## 4. Sub-Domain Coverage Audit

### 4.1 Environmental Control
**In source:**
- thermostat current reading
- thermostat set point
- thermostat sensing range
- humidistat current reading
- humidistat set point

**Missing or vague:**
- thermostat set-point range and increments
- humidistat range and increments
- daily schedule period structure
- manual overrides
- HVAC/humidifier compatibility model

### 4.2 Security & Safety
**In source:**
- magnetic contact switches for doors/windows
- sound/light alarms
- breach trigger from magnetic contact

**Missing or vague:**
- arm/disarm states
- trigger rules
- reset/acknowledgement
- communication-loss fail-safe behavior

### 4.3 Appliance & Power Management
**In source:**
- state monitoring for appliance power switches
- remote on/off control

**Missing or vague:**
- power ratings and safety limits
- default behavior after restart/failure
- explicit handling for lighting vs appliance categories

### 4.4 Planning & Reporting
**In source:**
- storage of plans and data
- backup service

**Confirmed by stakeholder as required:**
- monthly planner
- daily presets/schedules
- historical reports
- averages
- min/max
- downtime logs

**Still missing:**
- report retention period
- data export/print needs
- reporting granularity by device/type/date range

### 4.5 Non-Functional & QoS
**In source:**
- web-based access
- gateway RF module
- broadband Internet connection
- indoor RF range up to 1000 feet

**Missing or vague:**
- UI refresh rate
- sample rate in Hz
- command latency
- MTBF/failure-rate targets
- backup/recovery procedure details
- TLS encryption requirement

## 5. Documented Assumptions

Per instruction, minor or secondary gaps not escalated to the stakeholder are resolved here as explicit working assumptions for the elicitation record. These are **not new requirements** and must be validated later if the project proceeds beyond prototype definition.

1. **Prototype boundary assumption:** because the source repeatedly states the system is a limited prototype in a simulated environment, all device interactions are assumed to be simulation-driven rather than connected to physical hardware.
2. **Role model assumption:** the system supports three roles only—General User, Master User, and DH Technician—as stated in the source. Master User and DH Technician are assumed to have equivalent configuration privileges unless a later specification differentiates them.
3. **Access control assumption:** since distinct roles are described in the source, role-based access restrictions are assumed at a coarse level even though a detailed permission matrix is absent.
4. **Authentication assumption:** login is based on username/password only, because that is the only security baseline confirmed by the stakeholder.
5. **Transport security assumption:** TLS/HTTPS is not confirmed and therefore cannot be treated as a mandatory requirement from the current source set.
6. **Planning assumption:** monthly planning, daily presets/schedules, and historical reporting are in scope because the stakeholder explicitly confirmed all three.
7. **Report content assumption:** historical reports are assumed to cover at least the in-scope monitored domains where data exists (temperature, humidity, security events, and power/device state), but detailed report layouts are not defined.
8. **Backup assumption:** the home web server provides backup capability for user account information, user plans, and the home database, but backup frequency and recovery objectives are not specified.
9. **Lighting scope assumption:** lighting is mentioned at a high level with power management, but no distinct lighting-specific behavior beyond power switching is currently assumed.
10. **Safety assumption:** because the prototype is simulated, real-world electrical certification and physical hazard controls are outside prototype implementation scope, though logical power-state constraints remain relevant.
11. **RF range assumption:** the stated 1000-foot indoor range is treated as a high-level environmental target from the source, even though no throughput, interference, or reliability criteria are provided.
12. **Scheduling assumption:** daily presets/schedules are assumed to apply to controllable device categories where set points or power states can be scheduled, but exact schedule structure is unspecified.

## 6. Recommended Follow-On Clarifications for Future Specification Iterations

These items were not asked due to the 3-question limit and the instruction to focus only on critical high-level scope. They should be addressed in the next refinement round:

1. Define coarse permission matrix per role for monitoring, control, planning, reporting, account management, parameter configuration, and system start/stop.
2. Define thermostat and humidistat set-point ranges, increments, deadbands, and override behavior.
3. Define security operating modes and alarm reset behavior.
4. Define appliance categories and power/load limits for simulated switches.
5. Define measurable QoS targets: refresh rates, sample rates, latency, reliability, and backup/recovery expectations.
6. Clarify whether secure transport (TLS/HTTPS) is required despite the minimal username/password baseline.

## 7. Final Elicitation Summary

The source document provides a credible high-level prototype concept, but it is intentionally incomplete and leaves many operational rules unquantified. The most important clarifications obtained were:
- planning/reporting is in scope and includes monthly planner, daily presets, and historical reports;
- authentication baseline is username/password;
- user roles remain as already defined in the source.

However, the specification still contains substantial ambiguity in access-control detail, environmental control rules, alarm/fail-safe behavior, appliance safety constraints, and measurable non-functional targets. These gaps should be treated as significant risks for design completeness, testability, and acceptance criteria unless refined in subsequent specification work.
