#let chatgpt_go_by(body) = (
  smallcaps()[
    #highlight(fill: rgb("#EDE8BA"))[*ChatGPT go-by*] #linebreak()
  ] +
  box(fill: rgb("#EDE8BA"), outset: 3pt)[
    #body
  ] +
  [
    \
  ]
)

#set page(
  header: [_Group 12_ #h(1fr) SPIDAM - Final Report],
  numbering: "1"
)

#let title_page = [
  #set align(center + horizon)
  
  Scientific Python Interactive Data Acoustic Modeling \
  https://github.com/jhw-0/spidam_group_12
  \
  \
  \
  = Project Report
  == COP 2080 \ Florida Polytechnic University \ Fall 2024
  \
  \
  \
  *_submitted by_*: \
  _Group 12_ \
  Jared Wallace - Applied mathematics student \
  Chris Lawrence - Cybersecurity student
  \
  \
  \
  *_submitted to_*: \
  Christian Navarro \
  December 1#super("st"), 2024

  #pagebreak()
]
#title_page

#set text(
  font: "Libertinus Serif",
  size: 11pt,
)

#show heading: it => [
  #set text(size: 11pt)
  #it
]

#set heading(numbering: "1.1")

// 2-3 paragraphs describing your project, activities completed, highlights, learning experiences, your final product, and concluding remarks
= Introduction
// Paragraph 1: Describe project

Our project consisted of developing the Scientific Python Interactive Data Acoustic Modeling (SPIDAM) program, a corresponding report (this report) for our stakeholders (instructor and/or graders), and instances of team development tools we used along the way to reinforce a collaborative environment. SPIDAM, like its spelled-out form suggests, is an interactive data analysis and modeling platform that allows professionals to model acoustic data in various ways from a graphical user interface (GUI). This report not only describes important technical aspects of SPIDAM, but it also describes the instances of team development tools used during the completion of the project.

// Paragraph 2: Describe activities, learning experience, highlights

Throughout the project, we engaged in various activities such as recording our test audio, setting up an Asana board, creating a remote Git repository on GitHub, programming our version of the SPIDAM platform, and collaborating through text and phone to divide, plan, and implement project tasks. Each activity had a unique learning experience associated with it. Setting up a Git repository and making regular commits to it as a team reinforced through practice what we had learned during class and on prior assignments; and, even though our workflows and commit histories were demonstrably lacking experience, we gained confidence in using Git, and version control more generally, to be able to leverage this wisdom for future collaborative coding projects. This previously described learning experience was just as true for many other activities completed during the project, namely the activities of implementing a Model-View-Controller (MVC) pattern and utilizing an Asana board with a flavor of Agile practices in the form of user-stories. Likewise, a highlight of this project was gaining firsthand experience of important complexities of collaborative work, and similarly, getting to practice solving these complex issues using popular methods.

// Paragraph 3: Describe final product and concluding remarks
Our final deliverables were comprised of a working directory as a Python program, a sample audio recording in `.wav` format, a log of our git commits, and this project report. In reflection as a group, we are happy with how the SPIDAM deliverable turned out, but we are curious with how it would turn out if we had used different methods, libraries, or had used different patterns than MVC.

// 1 paragraph describing the business needs based on input from the professor. include an example including a brief desription of the proposed project's purpose, goals, and scope as well as rough order of magnitude estimate for schedule, and basic technical skill requirements
== Business Needs
// Paragraph 1:
A general business need for SPIDAM is for an automated tool that professionals can leverage to analyze and model acoustic data. For SPIDAM specifically, the primary business need is the need to analyze this acoustic data as it relates to voice intelligibility in enclosed spaces. Two important, but secondary to the former, business needs are outlined in the user-story epics outlined in Section 2 and are, briefly, (1) the capability of the SPIDAM platform to enable users to remain focused on their expertise rather than focusing on SPIDAM as a tool, and (2) the capability of the SPIDAM coding team, and therefore the SPIDAM code itself, to quickly respond to user-demands. Additional to the previous business needs related to functionality, is the need for a timely finished product. A working version of the SPIDAM platform was to be completed by the end of the day on December 1#super("st"), 2024. The technical skills needed by students working on this project included having a basic understanding of Git version control and agile concepts as implemented by Asana, object-oriented design in Python, and the ability to work collaboratively on large assignments to meet deadlines.

// 1 paragraph stating the engineering requirements stated by the professor or interpreted through business needs statements. Design objectives will be in the form of engineering requirements and are not subjective, stating what and how the data is to be measured
== Design Objectives
// Paragraph 1:
The primary design requirements of the SPIDAM platform is to use a Model-View-Controller design pattern for the top-level architecture of SPIDAM's Python program. Subsequently, this requires that state information be kept in the `Model` class, that what the user sees and interacts with is exactly what is in the `View` class, and that the flow of SPIDAM is managed by the `Controller` class. Additionally, it is required that all user interactions with the system are delegated to these aforementioned classes.

// describe the functional requirements of the project including user interface requirements
== Functional Requirements
// Paragraph 1:
The functional requirements of SPIDAM can be categorized into (1) importing and cleaning audio data, (2) analyzing and modeling data, and (3) reporting and visualizing data. Importing and cleaning audio data must consist of removing metadata, and priming the audio data, now by itself, to a standard format for later processing; the second of these steps, which requires exporting the audio to a single-channeled `.wav` file format. One part of analyzing and modeling the data must consist of displaying important scalar data from the audio, such as its length in seconds, and several frequency measurements in Hz--including the highest resonance frequency. The other part of analyzing and modeling data must consist of plotting the data in a user-friendly manner through waveform plots so that the user can visualize the data. The last category of functional requirements can be summarized as an interactive GUI which the user of SPIDAM can interact with through the use of interactive elements, such as buttons, to load data and change parameters affecting the downstream analysis and presentation.

// describe the major assumptions and limitations of the project
== Limitations
// Paragraph 1:
From the perspective of designing and developing the SPIDAM platform, limitations included time constraints, student experience with collaboration processes and tools, and library limitations with respect to design and functional requirements. For example, one particular limitation of using `tkinter` within an MVC pattern is in separating view and controller units when both types of units are children of a `Tk()` instance. Despite our solution, we extrapolate that future modifications to SPIDAM could still be limited by the need to actively decouple the classes. Apart from the persepctive of designing and developing SPIDAM, there are also limitations on achieving an analysis that truthfully represents the real world measurements fed into the SPIDAM platform. An example of such limitations include presenting the data at a granularity that is convenient for the user, yet feasible to program. For instance, visualizations of the data in SPIDAM are inherently summaries of the audio data, and furthermore, attempts to allow the user to overcome this by giving them more options could still be limited, especially in cases where an overestimate in what the user needs causes necessary complexity.

= Agile User Stories
- *Epic 1*: As a user of SPIDAM, I want a program written for my purposes so that I can remain focused on my expertise.
  - *User story 1*: As a user of SPIDAM, I want to be able to analyze my data without needing to write nor understand Python libraries and code, so that I can focus on my job and not the tools beneath it.
  - *User story 2*: As a user of SPIDAM, I want an intuitive user interface, so that I can maintain my focus on analyzing acoustic data rather than experimenting or browsing documentation.
  - *User story 3*: As a user of SPIDAM, I want a well-tested program, so that a faulty analysis doesn't cause downstream issues.
- *Epic 2*: As a developer of SPIDAM, I want to focus on development tasks so that I can use my limited time to develop a better product.
  - *User story 1*: As a developer of SPIDAM, I want to be able to come back to my code and understand it, so that I spend as much time as possible writing code.
  - *User story 2*: As a developer of SPIDAM, I want to be able to hand off tasks and quickly on-board new maintainers so that the development of SPIDAM can leverage a team effort to get more done.
  - *User story 3*: As a developer of SPIDAM, I want expressive and robust units of code, so that I have the ability to quickly test, add new features, and reproduce results without spending time rewriting foundational code.

// State the location of your audio recording. Show a wide image that includes the space recorded such as a room or hall, and the person creating the clap. State the numberical output from your measurements and show screenshots of all plots, tables, etc.
= Results

// Paragraph 1:
#chatgpt_go_by()[
  We conducted our audio recording in the Aula Magna auditorium on campus, an enclosed space known for its long reverberation times. A wide-angle photograph of the auditorium was taken, showing the seating area, stage, and the person performing the hand clap at a distance of 3 meters from the recording device placed at the center aisle. The analysis of the recorded audio sample yielded an overall RT60 value of 1.8 seconds. The RT60 values across the frequency ranges were as follows: low frequencies (20 Hz – 500 Hz) had an RT60 of 2.1 seconds, mid frequencies (500 Hz – 2 kHz) had an RT60 of 1.7 seconds, and high frequencies (2 kHz – 20 kHz) had an RT60 of 1.4 seconds. The frequency with the greatest amplitude was identified at 315 Hz, indicating a significant resonance in the low-frequency range. Screenshots of the waveform plot, RT60 plots for each frequency range, and an overlapping plot of RT60 values were generated and included in the results.
]
...

#figure(
  image("clap.png"),
  caption: [
    The audio recording, consisting of a clap with reverberations, took place in the Aula Magna room in the Innovation, Science, and Technology building on the Florida Polytechnic campus.
  ]
)

// This section should describe how you tested your final product and your results. Did your product meet the design objectives and specifications? If they did great, if they didn't, why?
= Final Product Testing
// Paragraph 1:
#chatgpt_go_by()[
  To test our final product, we conducted a series of functional and performance tests. We verified the application's ability to load audio files in both WAV and MP3 formats, ensuring that non-WAV files were correctly converted. We tested the metadata removal and multi-channel handling features using audio files with varying properties. The data analysis functions were validated by comparing computed RT60 values with expected results from sample data. The GUI was tested for usability, ensuring all buttons and plots functioned as intended. Our product met the design objectives and specifications, successfully measuring and analyzing RT60 values across the specified frequency ranges and providing the required visualizations and textual outputs. Any minor discrepancies were addressed through iterative debugging and refinement.
]
...

// Summarize your team's efforts and results of this project.
= Conclusions and Project Summary
// Paragraph 1: Short summary of John A. Doe's contributions and how they resulted in project deliverables.
#chatgpt_go_by()[
  John A. Doe contributed significantly to the development of the data analysis and modeling components of the project. He was responsible for implementing the RT60 calculation algorithms using Python libraries such as SciPy and LibROSA. His work ensured accurate measurement of reverberation times across the frequency ranges. John also developed the data visualization modules, creating plots for the waveform and RT60 values. His contributions were critical in producing the analytical and graphical outputs required for the project deliverables.
]
...

// Paragraph 2: Short summary of John B. Doe's contributions and how they resulted in project deliverables.
#chatgpt_go_by()[
  John B. Doe focused on the development of the graphical user interface and the overall application structure following the Model-View-Controller (MVC) design pattern. He designed the GUI using Tkinter, ensuring it was intuitive and met all functional requirements. John also handled the data cleaning processes, including audio format conversion, metadata removal, and multi-channel processing. His efforts in organizing the codebase and implementing version control with GitHub were essential for team collaboration and project management, resulting in a well-structured and user-friendly application.
]
...

// This section should have a table with a percentage for each group members contribution.
== Individual Contribution Table
// Paragraph 1: reference the table
#chatgpt_go_by()[
  
]
...

// Each group member should write a 1-2 paragraph individual contribution section to discuss what you contributed
== Individual Contribution Reports

=== John A. Doe Account of Individual Contributions
// Paragraph 1: What you contributed category 2
#chatgpt_go_by()[
  I was primarily responsible for implementing the acoustic data analysis and modeling components of the project. I developed algorithms for calculating RT60 values using the Schroeder integral method and ensured accurate computations across the low, mid, and high-frequency ranges. Utilizing libraries such as SciPy and LibROSA, I processed the audio signals and performed the necessary signal processing tasks.
]
...

// Paragraph 2: What you contributed category 2
#chatgpt_go_by()[
  In addition to the analytical computations, I focused on creating the data visualization elements of the application. I designed and implemented plotting functions using Matplotlib, generating visual representations of the audio waveform and RT60 values. These visualizations were integrated into the GUI, enhancing the user's ability to interpret the results. My contributions were instrumental in delivering the core analytical functionality of the SPIDAM application.
]
...

=== John B. Doe's Account of Individual Contributions
// Paragraph 1: What you contributed category 2
#chatgpt_go_by()[
  I was primarily responsible for designing and developing the graphical user interface (GUI) of the SPIDAM application. Using Tkinter, I created an intuitive and user-friendly interface that met all functional requirements, including buttons for loading files, displaying plots, and presenting textual outputs. I ensured that the GUI followed the Model-View-Controller (MVC) design pattern for efficient code organization.
]
...

// Paragraph 2: What you contributed category 2
#chatgpt_go_by()[
  I also handled the data cleaning processes required before analysis. This included implementing functions to convert audio files from MP3 to WAV format, remove metadata, and handle multi-channel audio by converting it to a single channel when necessary. Furthermore, I managed the project's version control system using Git and GitHub, coordinating the branching and merging processes to facilitate team collaboration. My contributions were essential in providing a seamless user experience and maintaining the project's structural integrity.
]
...

// Each group member should write a 2-3 paragraph reflection report from each member. What did you learn from this project? What worked well? What was most challenging?
== Individual Reflection Reports

=== John A. Doe Reflection Report
// Paragraph 1: What did you learn from this project?
#chatgpt_go_by()[
  Working on the SPIDAM project was an enriching experience that deepened my understanding of acoustic modeling and signal processing. I learned how to apply theoretical concepts of reverberation time and frequency analysis using practical tools like Python and its scientific libraries. The process of implementing RT60 calculations and ensuring their accuracy was both challenging and rewarding.
]
...

// Paragraph 2: What worked well?
#chatgpt_go_by()[
  One aspect that worked well was our team's collaboration and division of tasks based on our strengths. We maintained clear communication and utilized version control effectively, which streamlined our development process. The integration of different components, such as data analysis and GUI, was smooth due to our adherence to the MVC design pattern.
]
...

// Paragraph 3: What was most challenging?
#chatgpt_go_by()[
  The most challenging part was handling the nuances of audio data processing, particularly in dealing with background noise and ensuring the reliability of our RT60 measurements. We had to iterate on our algorithms and refine our data cleaning methods to improve accuracy. Overall, this project enhanced my problem-solving skills and provided valuable experience in applying computational methods to real-world acoustic problems.
]
...

=== John B. Doe Reflection Report
// Paragraph 1: What did you learn from this project?
#chatgpt_go_by()[
  Participating in the SPIDAM project allowed me to enhance my skills in GUI development and software architecture. I gained a deeper appreciation for the importance of user experience in software applications. Designing an interface that is both functional and intuitive required careful consideration of user interactions and feedback mechanisms.
]
...

// Paragraph 2: What worked well?
#chatgpt_go_by()[
  Our team's effective use of version control and adherence to coding standards contributed significantly to the project's success. The MVC design pattern facilitated clear separation of concerns, making the codebase more maintainable and scalable. Collaborating closely with John A. Doe on integrating the data analysis components into the GUI was a highlight of the project.
]
...

// Paragraph 3: What was most challenging?
#chatgpt_go_by()[
  The most challenging aspect was ensuring compatibility across different systems and handling various audio file formats and properties. Implementing robust error handling and data validation required meticulous attention to detail. This project taught me the value of thorough testing and the importance of anticipating user needs and potential issues. Overall, it was a valuable learning experience in software development and team collaboration.
]
...
