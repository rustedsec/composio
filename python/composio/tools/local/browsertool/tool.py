"""
Browser tool for Composio.
"""

import typing as t

from composio.tools.base.local import LocalAction, LocalTool

from .actions import (
    ClickElement,
    GetElementDetails,
    GetPageDetails,
    GetScreenshot,
    GotoPage,
    NavigateHistory,
    RefreshPage,
    ScrollPage,
    TypeText,
)


class BrowserTool(LocalTool, autoload=True):
    """Browser tool for local usage."""

    @classmethod
    def actions(cls) -> t.List[t.Type[LocalAction]]:
        """Return the list of actions."""
        return [
            GetScreenshot,
            GetPageDetails,
            ClickElement,
            GetElementDetails,
            NavigateHistory,
            RefreshPage,
            ScrollPage,
            TypeText,
            GotoPage,
        ]