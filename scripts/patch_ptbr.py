import json, pathlib
pt_path = pathlib.Path("F:/Dev/Pixel-Office/locales/pt-BR.json")
pt2_path = pathlib.Path("F:/Dev/Pixel-Office/locales/pt.json")
pt = json.loads(pt_path.read_text(encoding='utf-8'))

patches = {
    'ui.chat.placeholder': 'Dê uma tarefa ou faça uma pergunta…',
    'ui.chat.hint': 'Enter envia · Shift+Enter nova linha · Ctrl+V cola imagem · Esc fecha',
    'ui.chat.offlineNote': 'Sem conexão com o servidor. O que você digitar fica aqui; envie quando a conexão voltar.',
    'ui.chat.profile': 'Perfil, memória, habilidades',
    'ui.chat.stop': 'Interromper tarefa',
    'ui.chat.reset': 'Resetar o chat (memória permanece) — clique duas vezes',
    'ui.chat.close': 'Fechar (Esc)',
    'ui.chat.today': 'Hoje',
    'ui.chat.older': 'Carregar mensagens anteriores',
    'ui.chat.actions': '{n} ações',
    'ui.chat.actions_one': '{n} ação',
    'ui.chat.permission': '🔐 Solicitação de permissão',
    'ui.chat.allow': 'Permitir',
    'ui.chat.deny': 'Negar',
    'ui.chat.always': 'Sempre permitir',
    'ui.board.title': 'Quadro',
    'ui.board.button': 'Quadro',
    'ui.board.buttonTip': 'Tarefas e caderno compartilhado',
    'ui.board.tabTasks': 'Tarefas',
    'ui.board.tabNotes': 'Caderno compartilhado',
    'ui.board.newTask': 'Nova tarefa',
    'ui.board.taskTitle': 'Título',
    'ui.board.taskDetail': 'O que se espera, escopo, dependências',
    'ui.board.owner': 'Responsável',
    'ui.board.add': 'Adicionar ao quadro',
    'ui.board.close': 'Fechar',
    'ui.board.saved': 'Salvo',
    'ui.board.save': 'Salvar',
    'ui.board.cancel': 'Cancelar',
    'ui.board.edit': 'Editar',
    'ui.board.delete': 'Excluir',
    'ui.costs.title': 'Custos',
    'ui.costs.close': 'Fechar',
    'ui.progress.title': 'Progresso',
    'ui.progress.close': 'Fechar',
    'ui.activity.title': 'Atividade',
    'ui.activity.close': 'Fechar',
    'ui.inbox.title': 'Aguardando você',
    'ui.welcome.title': 'Bem-vindo ao seu escritório',
    'ui.welcome.cta': 'Vamos lá',
    'ui.meeting.button': 'Reunião',
    'ui.meeting.buttonTip': 'Convocar reunião',
    'ui.settings.title': 'Configurações',
    'ui.settings.close': 'Fechar',
    'ui.settings.saved': 'Salvo',
    'ui.settings.tabs.general': 'Geral',
    'ui.settings.tabs.offices': 'Escritórios',
    'ui.settings.tabs.models': 'Modelos',
    'ui.settings.tabs.server': 'Servidor',
    'ui.settings.lang': 'Idioma',
    'ui.hire.crumb': 'Contratar',
    'ui.hire.back': '← Voltar ao escritório',
    'server.busy': 'funcionário ocupado',
    'server.noMemory': 'sem arquivo de memória',
    'server.duplicateId': 'ID do funcionário "{id}" já está em uso',
    'server.notFound': 'não encontrado',
    'server.stoppedByUser': 'O usuário interrompeu a tarefa.',
    'server.stopped': 'Interrompido.',
    'server.sessionError': 'Erro de sessão.',
    'server.cancelled': 'Cancelado.',
    'server.textRequired': 'texto é obrigatório',
    'server.nameRoleRequired': 'nome e cargo são obrigatórios',
    'status.idle': 'ocioso',
    'status.working': 'trabalhando',
    'status.waiting': 'aguardando você',
    'status.error': 'erro',
    'status.sick': 'doente',
}

def set_path(obj, path, value):
    parts = path.split('.')
    cur = obj
    for p in parts[:-1]:
        cur = cur[p]
    cur[parts[-1]] = value

for k,v in patches.items():
    try:
        set_path(pt, k, v)
        print(f'patched {k}')
    except Exception as e:
        print(f'FAIL {k}: {e}')

pt['name']='Português (Brasil)'
pt_path.write_text(json.dumps(pt, ensure_ascii=False, indent=2), encoding='utf-8')
pt2_path.write_text(json.dumps(pt, ensure_ascii=False, indent=2), encoding='utf-8')
print('Salvo')
for k in ['ui.chat.placeholder','ui.board.title','ui.board.tabTasks','ui.settings.title','server.busy','status.idle']:
    cur=pt
    for p in k.split('.'):
        cur=cur[p]
    print(k, repr(cur))
