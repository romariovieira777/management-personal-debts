import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.src.config.config import Base


class AttachmentModel(Base):
    __tablename__ = 'tb_attachments'

    id = Column(Integer, primary_key=True, index=True)
    debt_id = Column(Integer, ForeignKey('tb_debts.id'), nullable=False, index=True)
    file_name = Column(String(255), nullable=False)
    file_path = Column(String(512), nullable=False)
    mime_type = Column(String(127), nullable=False)
    file_size = Column(Integer, nullable=False)
    uploaded_at = Column(DateTime, nullable=False, default=lambda: datetime.datetime.now())

    debt = relationship("DebtsModel", back_populates="attachments")

    def __repr__(self):
        return f"<Attachment {self.file_name}>"

    @property
    def file_size_formatted(self):
        """Retorna o tamanho do arquivo em formato legível"""
        size = self.file_size
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024:
                return f"{size:.2f} {unit}"
            size /= 1024
        return f"{size:.2f} TB"

    @property
    def is_image(self):
        """Verifica se o anexo é uma imagem"""
        return self.mime_type.startswith('image/')

    @property
    def is_document(self):
        """Verifica se o anexo é um documento"""
        document_types = ['application/pdf', 'application/msword',
                         'application/vnd.openxmlformats-officedocument']
        return any(self.mime_type.startswith(t) for t in document_types)