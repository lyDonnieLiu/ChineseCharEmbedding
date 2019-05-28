USE [test]
GO
/****** Object:  Table [dbo].[course]    Script Date: 2019-04-17 下午 3:36:05 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[course](
	[course_id] [varchar](8) NOT NULL,
	[title] [varchar](50) NULL,
	[dept_name] [varchar](20) NULL,
	[credits] [numeric](2, 0) NULL,
PRIMARY KEY CLUSTERED 
(
	[course_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
SET ANSI_PADDING OFF
GO
/****** Object:  Table [dbo].[prereq]    Script Date: 2019-04-17 下午 3:36:05 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[prereq](
	[course_id] [varchar](8) NOT NULL,
	[prereq_id] [varchar](8) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[course_id] ASC,
	[prereq_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
SET ANSI_PADDING OFF
GO
INSERT [dbo].[course] ([course_id], [title], [dept_name], [credits]) VALUES (N'BIO-101', N'Intro. to Biology', N'Biology', CAST(4 AS Numeric(2, 0)))
INSERT [dbo].[course] ([course_id], [title], [dept_name], [credits]) VALUES (N'BIO-301', N'Genetics', N'Biology', CAST(4 AS Numeric(2, 0)))
INSERT [dbo].[course] ([course_id], [title], [dept_name], [credits]) VALUES (N'BIO-399', N'Computational Biology', N'Biology', CAST(3 AS Numeric(2, 0)))
INSERT [dbo].[course] ([course_id], [title], [dept_name], [credits]) VALUES (N'CS-101', N'Intro. to Computer Science', N'Comp. Sci.', CAST(4 AS Numeric(2, 0)))
INSERT [dbo].[course] ([course_id], [title], [dept_name], [credits]) VALUES (N'CS-190', N'Game Design', N'Comp. Sci.', CAST(4 AS Numeric(2, 0)))
INSERT [dbo].[course] ([course_id], [title], [dept_name], [credits]) VALUES (N'CS-315', N'Robotics', N'Comp. Sci.', CAST(3 AS Numeric(2, 0)))
INSERT [dbo].[course] ([course_id], [title], [dept_name], [credits]) VALUES (N'CS-319', N'Image Processing', N'Comp. Sci.', CAST(3 AS Numeric(2, 0)))
INSERT [dbo].[course] ([course_id], [title], [dept_name], [credits]) VALUES (N'CS-347', N'Database System Concepts', N'Comp. Sci.', CAST(3 AS Numeric(2, 0)))
INSERT [dbo].[course] ([course_id], [title], [dept_name], [credits]) VALUES (N'EE-181', N'Intro. to Digital Systems', N'Elec. Eng.', CAST(3 AS Numeric(2, 0)))
INSERT [dbo].[course] ([course_id], [title], [dept_name], [credits]) VALUES (N'FIN-201', N'Investment Banking', N'Finance', CAST(3 AS Numeric(2, 0)))
INSERT [dbo].[course] ([course_id], [title], [dept_name], [credits]) VALUES (N'HIS-351', N'World History', N'History', CAST(3 AS Numeric(2, 0)))
INSERT [dbo].[course] ([course_id], [title], [dept_name], [credits]) VALUES (N'MU-199', N'Music Video Production', N'Music', CAST(3 AS Numeric(2, 0)))
INSERT [dbo].[course] ([course_id], [title], [dept_name], [credits]) VALUES (N'PHY-101', N'Physical Principles', N'Physics', CAST(4 AS Numeric(2, 0)))
INSERT [dbo].[prereq] ([course_id], [prereq_id]) VALUES (N'BIO-301', N'BIO-101')
INSERT [dbo].[prereq] ([course_id], [prereq_id]) VALUES (N'BIO-399', N'BIO-101')
INSERT [dbo].[prereq] ([course_id], [prereq_id]) VALUES (N'CS-190', N'CS-101')
INSERT [dbo].[prereq] ([course_id], [prereq_id]) VALUES (N'CS-315', N'CS-101')
INSERT [dbo].[prereq] ([course_id], [prereq_id]) VALUES (N'CS-319', N'CS-101')
INSERT [dbo].[prereq] ([course_id], [prereq_id]) VALUES (N'CS-347', N'CS-101')
INSERT [dbo].[prereq] ([course_id], [prereq_id]) VALUES (N'EE-181', N'PHY-101')
ALTER TABLE [dbo].[course]  WITH CHECK ADD FOREIGN KEY([dept_name])
REFERENCES [dbo].[department] ([dept_name])
ON DELETE SET NULL
GO
ALTER TABLE [dbo].[prereq]  WITH CHECK ADD FOREIGN KEY([course_id])
REFERENCES [dbo].[course] ([course_id])
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[prereq]  WITH CHECK ADD FOREIGN KEY([prereq_id])
REFERENCES [dbo].[course] ([course_id])
GO
ALTER TABLE [dbo].[course]  WITH CHECK ADD CHECK  (([credits]>(0)))
GO
