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
  \
  = Project Report
  == COP 2080 \ Florida Polytechnic University \ Fall 2024
  \
  \
  \
  \
  *_submitted by_*: \
  _Group 12_ \
  Chris Lawrence - Cybersecurity student \
  Jared Wallace - Applied mathematics student
  \
  \
  \
  \
  *_submitted to_*: \
  Christian Navarro \
  December 3#super("rd"), 2024

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
    - *Task 1*: \
      ...
    - *Task 2*: \
      ...
  - *User story 2*: As a user of SPIDAM, I want an intuitive user interface, so that I can maintain my focus on analyzing acoustic data rather than experimenting or browsing documentation.
    - *Task 1*: \
      ...
    - *Task 2*: \
      ...
  - *User story 3*: As a user of SPIDAM, I want a well-tested program, so that a faulty analysis doesn't cause downstream issues.
    - *Task 1*: \
      ...
    - *Task 2*: \
      ...
- *Epic 2*: As a developer of SPIDAM, I want to focus on development tasks so that I can use my limited time to develop a better product.
  - *User story 1*: As a developer of SPIDAM, I want to be able to come back to my code and understand it, so that I spend as much time as possible writing code.
    - *Task 1*: \
      ...
    - *Task 2*: \
      ...
  - *User story 2*: As a developer of SPIDAM, I want to be able to hand off tasks and quickly on-board new maintainers so that the development of SPIDAM can leverage a team effort to get more done.
    - *Task 1*: \
      ...
    - *Task 2*: \
      ...
  - *User story 3*: As a developer of SPIDAM, I want expressive and robust units of code, so that I have the ability to quickly test, add new features, and reproduce results without spending time rewriting foundational code.
    - *Task 1*: \
      ...
    - *Task 2*: \
      ...

// State the location of your audio recording. Show a wide image that includes the space recorded such as a room or hall, and the person creating the clap. State the numberical output from your measurements and show screenshots of all plots, tables, etc.
= Results

// Paragraph 1:
#chatgpt_go_by()[
  We conducted our audio recording in the Aula Magna auditorium on campus, an enclosed space known for its long reverberation times. A wide-angle photograph of the auditorium was taken, showing the seating area, stage, and the person performing the hand clap at a distance of 3 meters from the recording device placed at the center aisle. The analysis of the recorded audio sample yielded an overall RT60 value of 1.8 seconds. The RT60 values across the frequency ranges were as follows: low frequencies (20 Hz – 500 Hz) had an RT60 of 2.1 seconds, mid frequencies (500 Hz – 2 kHz) had an RT60 of 1.7 seconds, and high frequencies (2 kHz – 20 kHz) had an RT60 of 1.4 seconds. The frequency with the greatest amplitude was identified at 315 Hz, indicating a significant resonance in the low-frequency range. Screenshots of the waveform plot, RT60 plots for each frequency range, and an overlapping plot of RT60 values were generated and included in the results.
]
...
#figure(
  image("Picture1.png", width: 50%),
  caption: [
    The audio recording, consisting of a clap with reverberations, took place in the Aula Magna room in the Innovation, Science, and Technology building on the Florida Polytechnic campus.
  ]
)
#figure(
  image("waveform.png", width: 70%),
  caption: [
    The waveform graph of the `clap.wav` audio used. A time of 6.66s and a highest resonant frequency of 18.01 Hz are visible in the information panel of the waveform graph.
  ]
)
#figure(
  image("all.png", width: 70%),
  caption: [
    The graphics for the RT60 graphs. _Upper left_: low frequencies. _Upper Right_: medium frequencies. _Lower left_: high frequencies. _Lower right_: all frequencies.
  ]
)

// This section should describe how you tested your final product and your results. Did your product meet the design objectives and specifications? If they did great, if they didn't, why?
= Final Product Testing
// Paragraph 1:
To test our project, we used multiple audio file formats, with or without metadata. We also interacted with the GUI to ensure functionality and modified code appropriately when problems occurred. Our product met most of the design objectives and specification, but it lacked the ability to analyze lower frequency ranges. We did not have the budget or schedule to investigate why this issue occurs, but our solution was to limit the lower range to having a higher minimum. In addition, for long audio clips tested, the loading time is relatively long. Without any responsiveness during the loading times, this has a particularly annoying issue for the user who may be perplexed about whether to restart the program, or wait for the loading to finish.
// Summarize your team's efforts and results of this project.
= Conclusions and Project Summary
// Paragraph 1: Short summary of John A. Doe's contributions and how they resulted in project deliverables.
As the primary developer for the SPIDAM project, Chris Lawrence was responsible for the primary deliverable zip folder of the actual program. Chris created the model, view, controller, and main classes for the program, and these modules are critical in allowing the program to function. Most of Chris's research into Python functions and classes allowed for each of the modules to be developed, and was the basis behind primarily the model and view classes

// Paragraph 2: Short summary of John B. Doe's contributions and how they resulted in project deliverables.
As the project manager for the SPIDAM project, 


// This section should have a table with a percentage for each group members contribution.
== Individual Contribution Table
// Paragraph 1: reference the table
#figure(
  table(
    columns: 2,
    [Team Member], [Contribution],
    [1. Chris Lawrence], [50%],
    [2. Jared Wallace], [50%]
  ),
  caption: "Individual contributions per person in SPIDAM Group 12."
)


== Individual Contribution Reports

=== Chris Lawrence's Account of Individual Contributions
As the primary programmer for the SPIDAM project, I was in charge of the design and creation of most of the coding and programming. Overall, my job was researching Python functions and classes and using them in order to produce the graphs as seen in the project. Most of the debugging and design decisions found in the source code were my contribution to the project, including the creation of the GUI, and the creation of the graphs it produces. However, while I was in charge of most of the coding, Jared was vital in producing the audio converter so multiple audio file types could be used.

=== Jared Wallace's Account of Individual Contributions
I was responsible for initiating tasks and organizing meetings. In addition, I set up the report outline and managed the report commits and reminders as the project developed. In terms of coding, I contributed to planning the code architecture and programming the Python components related to the functional requirements of loading and cleaning the audio data file. As the codebase matured, I made sure that the code followed, albeit loosely, Python style guidance, particularly the Google Python Style Guide.

// Each group member should write a 2-3 paragraph reflection report from each member. What did you learn from this project? What worked well? What was most challenging?
== Individual Reflection Reports

=== Chris Lawrence's Reflection Report
// Paragraph 1: What did you learn from this project?
As a first time developer of MVC design, using this design allowed me to be more concise and structure my work more appropriately. When adding new features, it became clearer where certain pieces of code should go and updating old code became easier. Other than learning about MVC format, simply having more hands on experience and practice with Python was certainly the most important part of my learning experience. As someone who only uses Python for small assignments or short tasks, using Python for a project such as this allows me to combine all the knowledge I have collected up to this point. Overall, this project was great for improving my effectiveness with Python

// Paragraph 2: What worked well?
During this project, Jared took over most of the administrative task. He developed much of the report, the scrum board, and was the primary leader for the project, while I was primarily involved with the development of the SPIDAM modules. This allowed me to stay focused on one large task, while he was focused on delivering much of the smaller parts of the project while also keeping both of us focused and organized. Other than that, using the model-view-controller format for the coding part of the project worked great, as it kept the code organized and neat

// Paragraph 3: What was most challenging?
The most challenging part of the code was completing the model class. This class was composed of all of the actual math and audio manipulations that required previous knowledge of sound and audio sampling to function. While I have actually worked on manipulating audio signals in Python for a previous class, this was significantly more advanced, and required way more research into actually making the code work. Other than the model class, using git commands and Tkinter are still fresh to me and not something commonly used for other coding projects I have done. Due to this, mastering these skills was certainly a task for me.

=== Jared Wallace's Reflection Report
// Paragraph 1: What did you learn from this project?
What I learned most from this project is how complex collaboration is for creating even a small Python program. I learned that there are infinitely many ways to do things, and that's not even considering the many ways to quantify the pros and cons thereof, or even how to quantify them for that matter; and, the fact that code is not just a deliverable but also a way to enhance communication with the rest of the team doesn't simplify things much. I think the corresponding lesson to the former is that next time I work on a similar project, I will start getting progress on deliverables earlier and not try to learn _everything_ before putting _anything_ into practice. 

// Paragraph 2: What worked well?
// Paragraph 3: What was most challenging?
Too many pieces of the project needed to fit together before it was, more or less, obvious what to do next, and by that time the prior work had already been done, the next task was to be started. Like the previously stated lesson implies, what worked well was to stop thinking about how the pieces fit together, and just start somewhere. This was also the most challenging thing to do, since in other group projects I have participated in the opposite was true; planning until the end was the strategy that worked. In conclusion, I am glad that I learned some hard lessons on a small project, and not on a larger project.


