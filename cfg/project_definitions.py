import os
import uuid


class ProjectDefinitions:

    __PROGRAM_SESSION_ID = None

    __CFG_DIR = os.path.dirname(os.path.abspath(__file__))

    __ROOT_DIR = os.path.join(
        __CFG_DIR,
        "..",
    )

    @staticmethod
    def getCFGDir():
        return ProjectDefinitions.__CFG_DIR

    @staticmethod
    def getROOTDir():
        return ProjectDefinitions.__ROOT_DIR

    @staticmethod
    def getProgramSessionID():
        if ProjectDefinitions.__PROGRAM_SESSION_ID == None:
            ProjectDefinitions.__PROGRAM_SESSION_ID = str(uuid.uuid4())

        return ProjectDefinitions.__PROGRAM_SESSION_ID


if __name__ == "__main__":
    print(ProjectDefinitions.getROOTDir())
    print(ProjectDefinitions.getProgramSessionID())
