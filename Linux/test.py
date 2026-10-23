import pytest
from unittest.mock import patch, AsyncMock, MagicMock
from load_saved_servers_ import load_saved_servers

# Тест 1: когда settings.LINK пуст — функция возвращает [], 0
@pytest.mark.asyncio
async def test_returns_empty_when_link_is_empty():
    with patch("load_saved_servers_.settings") as mock_settings:
        mock_settings.LINK = ""
        mock_settings.path_to_create_memory_file = "/tmp/nonexistent_file"
        
        with patch("load_saved_servers_.load_local_servers") as mock_load:
            mock_load.return_value = []
            
            result = await load_saved_servers()
            
            assert result == ([], 0)

# Тест 2: успешный сценарий
@pytest.mark.asyncio
async def test_continues_when_file_found():
    with patch("load_saved_servers_.settings") as mock_settings:
        mock_settings.LINK = "some_link"
        mock_settings.path_to_create_memory_file = "/tmp/test"
        
        with patch("load_saved_servers_.load_local_servers") as mock_load:
            mock_load.return_value = []
            
            with patch("load_saved_servers_.subscription.get_links") as mock_get_links:
                mock_get_links.return_value = (["link1"], 1)
                
                with patch("load_saved_servers_.subscription.get_clean_link") as mock_clean:
                    mock_clean.return_value = ["clean1"]
                    
                    with patch("load_saved_servers_.xray.get_dirty_json") as mock_dirty:
                        mock_dirty.return_value = ["dirty1"]
                        
                        with patch("load_saved_servers_.storage.create_file") as mock_create:
                            mock_create.return_value = (["final1"], 2)
                            
                            with patch("load_saved_servers_.xray.get_clean_json") as mock_clean_json:
                                mock_clean_json.return_value = None
                                
                                result = await load_saved_servers()
                                assert result == (["final1"], 2)

# Тест 3: проверка, что get_links НЕ вызывается, если LINK пуст
@pytest.mark.asyncio
async def test_does_not_call_get_links_when_empty():
    with patch("load_saved_servers_.settings") as mock_settings:
        mock_settings.LINK = ""
        mock_settings.path_to_create_memory_file = "/tmp/test"
        
        with patch("load_saved_servers_.load_local_servers") as mock_load:
            mock_load.return_value = []
            
            with patch("load_saved_servers_.subscription.get_links") as mock_get_links:
                result = await load_saved_servers()
                assert result == ([], 0)
                mock_get_links.assert_not_called()